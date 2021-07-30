# main.py

# standard library
import sys, os
import math

# pip packages
import numpy as np
import pandas as pd

# local modules
import d02_processing as preprocessor

if __name__ == "__main__":

    # csv paths
    trade_activity = '/data/01_raw/01_trade_activity.csv'
    ticker_metrics = '/data/01_raw/01_trade_activity.csv' 
    group_trades = '/data/02_intermediate/01_df_trade_activity.csv'
    processed_trades = '/data/03_processed/01_df_trade_processed.csv'

    # process input
    preprocessor.frame_data(csv_path=trade_activity, type="td")
    preprocessor.ticker_metrics(csv_path=trade_activity)

    # preprocess data | add features
    preprocessor.process.group_trades(csv_path=group_trades)
    preprocessor.process.convert_to_candle(csv_path=processed_trades)

    # view processed data
    grouped_trades = pd.read_csv(os.getcwd() + processed_trades)
    candle_stick_trades = pd.read_csv(os.getcwd() + processed_trades)