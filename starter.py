import pandas as pd
import numpy as np
import os

relative_path_data = "/sample_data/trade_activity.csv"
data_frame = pd.read_csv(os.getcwd() + relative_path_data, delimiter=",")
data_frame["Net Position"] = data_frame["Qty"] * data_frame["Price"]

open_trades = {}
complete_trades = []

for index, row in data_frame.iterrows():
    ticker = row["Symbol"]
    net_size = row["Qty"]
    net_position = row["Net Position"]
    if ticker in open_trades:
        open_trades[ticker]["net_size"] += net_size
        open_trades[ticker]["net_position"] += net_position
        if True if open_trades[ticker]["net_size"] == 0 else False:
            complete_trades.append([ticker, open_trades[ticker]["net_position"]])
            del open_trades[ticker]
    else:
        open_trades[ticker] = {"net_size": net_size, "net_position": net_position}

np_ar_v3 = np.round(np.asarray([-_[1] for _ in complete_trades]), decimals=1)
print(np_ar_v3)
print("Sum Total", np.sum(np_ar_v3))
print("Count", np.size(np_ar_v3))
