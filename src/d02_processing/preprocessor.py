# preprocessor.py

# standard library
import os

# pip packages
import pandas as pd
import numpy as np

def frame_data(csv_path: str, type: str):
    """
    summary:
        return dataframe w/workable datatypes
    args:
        csv_path (str): local path to csv
        type (str): broker
    returns:
        pd.DataFrame: [description]
    """
    df = pd.read_csv(os.getcwd() + csv_path, delimiter=",")
    df["Net Position"] = np.where(df["Spread"] == "STOCK",df["Qty"] * df["Net Price"],df["Qty"] * df["Net Price"] * 100)
    df["Exec Time"] = pd.to_datetime(df["Exec Time"])
    del df["Exp"]
    del df["Pos Effect"]
    del df["Price"]
    del df["Side"]
    del df["Order Type"]
    del df["Strike"]
    del df["Spread"]
    df.drop(df.columns[df.columns.str.contains("unnamed", case=False)],axis=1,inplace=True)
    df.to_csv(os.getcwd() + "/data/02_intermediate/01_df_trade_activity.csv",header=True,index=False)


# TODO : implement switch case statement to return data specific to type of import
def type_broker(type: str):
    switch = {1: td_ameritrade, 2: webull, 3: fidelity, 4: light_speed}

def td_ameritrade():
    pass

def webull():
    pass

def fidelity():
    pass

def light_speed():
    pass

def robin_hood():
    pass
