# process.py

#standard library
import datetime
import math
import os

#pip modules
import pandas as pd

balance = 2570

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
    target_columns = ["trade_num","ticker","profit_loss","cap","time_duration","positions","day","week","date","volume"]

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
                        volume
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

    # turn list into dataframe and export to csv
    df_churn = pd.DataFrame(data=complete_trades, index=range(len(complete_trades)), columns=target_columns)
    df_churn.to_csv(os.getcwd() + "/data/03_processed/01_df_trade_processed.csv",header=True,index=False)
