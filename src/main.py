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
    # process input
    preprocessor.frame_data(csv_path="/data/01_raw/01_trade_activity.csv", type="td")

    # preprocess data | add features
    preprocessor.process.group_trades(csv_path="/data/02_intermediate/01_df_trade_activity.csv")
    preprocessor.process.convert_to_candle(csv_path="/data/03_processed/01_df_trade_processed.csv")

    # view processed data
    grouped_trades = pd.read_csv(os.getcwd() + "/data/03_processed/01_df_trade_processed.csv").iloc[::-1]
    candle_stick_trades = pd.read_csv(os.getcwd() + "/data/03_processed/01_df_trade_candles.csv")

    print(grouped_trades.head())
    print(candle_stick_trades.head())