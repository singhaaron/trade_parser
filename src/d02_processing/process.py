# process.py

#standard library
import datetime
import math
import os
import re

#pip modules
import pandas as pd
import numpy as np

balance = 2670

def time_elapsed(start: datetime, end: datetime) -> int:
    """
    summary:
        helper method to take datetime object and return time elapsed from start to end of a position
    args:
        start: first element(time) of entry position
        end: last element(time) of exit position
    returns:
        pd.DataFrame: time duration from start to end of a postion
    """
    return end[-1].minute * 60 + end[-1].second - start[0].minute * 60 + start[0].second


def convert_to_candle(csv_path: str):
    global balance
    """
    summary: 
        convert csv w/parsed trades into daily candle data
    args:
        csv_path (str): path to parsed trade]
    """
    data = pd.read_csv(os.getcwd()+csv_path,delimiter=",").iloc[::-1]
    data.date = pd.to_datetime(data.date)

    daily_candles={}

    for index,row in data.iterrows():
        date = row['date']
        volume = row['volume']
        profit_loss = row['profit_loss']
        tmp_balance = balance
        balance = round(balance + profit_loss,2)
        if date in daily_candles:
            daily_candles[date]['volume'] += volume
            if balance > daily_candles[date]['high']:
                daily_candles[date]['high'] = balance
            elif balance < daily_candles[date]['low']:
                daily_candles[date]['low'] = balance 
            daily_candles[date]['close'] = balance
        else:
            daily_candles[date] = {
                'volume' : volume,
                'low' : tmp_balance,
                'high': tmp_balance,
                'open' : tmp_balance,
                'close' : balance,
                'date': date
            }
    candle_stick_data = pd.DataFrame.from_dict(daily_candles).transpose()
    candle_stick_data.to_csv(os.getcwd()+'/data/03_processed/01_df_trade_candles.csv',header=True,index=False)

def append_metrics(group_trades,metrics_table:str):
    """
    summary:
        returns dataframe after merging metrics dataframe with corresponding tickers in trade history 
    args:
        group_trades (pd.DataFrame): dataframe with proper formatted columns for type format
        metrics_table (str): path to where metrics file is stored
    returns:
        pd.DataFrame: merged dataframe with corresponding info
    """
    metrics_table = pd.read_csv(os.getcwd()+metrics_table, index_col=0,error_bad_lines=False)
    metrics_table['ticker'] = metrics_table.index
    group_trades = group_trades.merge(metrics_table[['ticker','Market Cap','Short Float','Shs Float']], on='ticker',how='left')
    return group_trades

def value_to_float(x):
    """
    summary:
        convert string to numeric float
    args:
        x(str): string with 'M' , 'K' , 'B' 
    returns:
        returns dtype(float) after converting string
    """
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    if 'T' in x:
        return float(x.replace('T', '')) * 1000000000000
    return 0.0

def classify_market_cap_range(x):
    """
    summary:
        categorize market capital
    args:
        x(float): market capital float
    returns:
        returns category(Str)
    """
    # Nano Cap: < 50,000,000
    # Micro Cap: range 50,000,000 - 300,000,000
    # Small Cap: 300,000,000 to 2,000,000,000
    # Mid Cap: 2,000,000,000 to 10,000,000,000
    if x == 0:
        return 'unknown'
    if x < value_to_float('50M'):
        return 'nano'
    if x > value_to_float('50M') and x < value_to_float('300M'):
        return 'micro'
    if x > value_to_float('300M') and x < value_to_float('2B'):
        return 'small'
    if x > value_to_float('2B') and x < value_to_float('10B'):
        return 'mid'
    if x > value_to_float('10B') and x < value_to_float('200B'):
        return 'large'
    if x > value_to_float('200B'):
        return 'mega'

def classify_metrics(data):
    """
    summary:
        categorize market cap
    args:
        x(str): string with 'M' , 'K' , 'B' 
    returns:
        returns dtype(float) after converting string
    """
    data['Market Cap'] = data['Market Cap'].astype(str)
    data['Market Cap'] = data['Market Cap'].apply(lambda x: re.sub(r'^-$', str(np.NaN), x))
    data['Market Cap'] = data['Market Cap'].replace(np.nan, 0)
    data['Market Cap Three'] = data['Market Cap'].apply(value_to_float)
    data['Market Category'] = data['Market Cap Three'].apply(classify_market_cap_range)
    del data["Market Cap Three"]
    return data

def group_trades(csv_path: str):
    """
    summary:
        return data frame w/condensed information and usable as a reflection of meaningful data
    args:
        df (pd.DataFrame): dataframe with proper formatted columns for type format
    returns:
        pd.DataFrame: dataframe with informated analyzed
    """
    df = pd.read_csv(os.getcwd() + csv_path, delimiter=",")
    df["Exec Time"] = pd.to_datetime(df["Exec Time"])

    open_trades = {}
    complete_trades = []
    target_columns = ["trade_num","ticker","profit_loss","cap","time_duration","positions","day","week","date","volume","entry","exit"]

    for index, row in df.iterrows():
        ticker = row["Symbol"]
        volume = abs(int(row["Qty"]))
        net_size = int(row["Qty"])
        net_position = row["Net Position"]
        net_cap = net_position if net_size > 0 else 0
        entrys = [row["Exec Time"]] if net_size > 0 else [0]
        exits = [row["Exec Time"]] if net_size < 0 else [0]
        if ticker in open_trades:
            open_trades[ticker]["volume"] += volume
            open_trades[ticker]["net_size"] += net_size
            open_trades[ticker]["net_position"] += net_position
            open_trades[ticker]["net_cap"] += net_cap
            open_trades[ticker]["executions"]["entrys"] += entrys
            open_trades[ticker]["executions"]["exits"] += exits
            if True if open_trades[ticker]["net_size"] == 0 else False:
                entrys = [_ for _ in open_trades[ticker]["executions"]["entrys"] if _ != 0]
                exits = [_ for _ in open_trades[ticker]["executions"]["exits"] if _ != 0]
                complete_trades.append(
                    [
                        len(complete_trades),
                        ticker,
                        -(round(open_trades[ticker]["net_position"], 2)),
                        round(open_trades[ticker]["net_cap"], 2),
                        time_elapsed(entrys, exits) if time_elapsed(entrys, exits) > 0 and time_elapsed(entrys, exits) < 1800 else 0,
                        len(entrys) + len(exits),
                        open_trades[ticker]["executions"]["exits"][0].day_of_week,
                        open_trades[ticker]["executions"]["exits"][0].strftime("%V"),
                        open_trades[ticker]["executions"]["exits"][0].date(),
                        volume,
                        entrys[0].time(),
                        exits[-1].time()
                    ]
                )
                del open_trades[ticker]
        else:
            open_trades[ticker] = {
                "volume": volume,
                "net_size": net_size,
                "net_position": net_position,
                "net_cap": net_cap,
                "executions": {"entrys": entrys, "exits": exits},
            }

    # export
    df_churn = pd.DataFrame(data=complete_trades, index=range(len(complete_trades)), columns=target_columns)
    oop = append_metrics(group_trades=df_churn,metrics_table='/data/02_intermediate/01_ticker_metrics_table.csv')
    oop = classify_metrics(data=oop)
    oop.to_csv(os.getcwd() + "/data/03_processed/01_df_trade_processed.csv",header=True,index=False)
