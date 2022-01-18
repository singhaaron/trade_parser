# main.py

# standard library
import sys, os
import math

# pip packages
import numpy as np
import pandas as pd

# local modules
import d02_processing as preprocessor
import d01_utils as stats_func

# csv paths
trade_activity = "/data/01_raw/01_trade_activity.csv"
ticker_metrics = "/data/01_raw/01_trade_activity.csv"
group_trades = "/data/02_intermediate/01_df_trade_activity.csv"
processed_trades = "/data/03_processed/01_df_trade_processed.csv"
candle_stick_trades = "/data/03_processed/01_df_trade_candles.csv"

def process_input():
    '''
    summary: set | trim data
    '''
    preprocessor.frame_data(csv_path=trade_activity, type="td")
    preprocessor.ticker_metrics(csv_path=trade_activity)

def preprocess_data():
    '''
    summary: preprocess data | add features
    '''
    preprocessor.process.group_trades(csv_path=group_trades)
    preprocessor.process.convert_to_candle(csv_path=processed_trades)

def view_processed_data():
    ''' 
    summary: view processed data
    '''
    grouped_trades = pd.read_csv(os.getcwd() + processed_trades)
    candle_stick_trades = pd.read_csv(os.getcwd() + processed_trades)

    print('Grouped Trades:')
    print(grouped_trades.head())
    print('CandleStick Trades:')
    print(candle_stick_trades.head())

def tmp_trade_journal():
    tmp = pd.read_csv(os.getcwd() + processed_trades)
    tmp['day'].replace({1:'tuesday',0:'monday',2:'wenesday',3:'thursday',4:'friday',},inplace=True)
    tmp['trade_num'] = tmp['trade_num'].values[::-1]
    tmp = tmp[['date','trade_num','ticker','Market Cap','Short Float','Shs Float','Market Category','entry','exit','time_duration','cap','positions','profit_loss']]
    tmp.to_csv('tmp.csv',header=True,index=False)

if __name__ == "__main__":
    process_input()
    preprocess_data()
    tmp_trade_journal()