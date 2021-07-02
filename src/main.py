# main.py

# standard library
import sys, os

# pip packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# local modules
import d02_processing as preprocessor

if __name__ == "__main__":
    # process input
    preprocessor.frame_data(csv_path="/data/01_raw/01_trade_activity.csv", type="td")
    # preprocess data | add features
    preprocessor.process.analyze(
        csv_path="/data/02_intermediate/01_df_trade_activity.csv"
    )
    # view processed data
    df_trades = pd.read_csv(
        os.getcwd() + "/data/03_processed/01_df_trade_processed.csv"
    )
