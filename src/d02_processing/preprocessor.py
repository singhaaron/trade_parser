# preprocessor.py
import pandas as pd
import numpy as np
import os


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
    data_frame = pd.read_csv(os.getcwd() + csv_path, delimiter=",")
    data_frame["Net Position"] = np.where(
        data_frame["Spread"] == "STOCK",
        data_frame["Qty"] * data_frame["Net Price"],
        data_frame["Qty"] * data_frame["Net Price"] * 100,
    )
    data_frame["Exec Time"] = pd.to_datetime(data_frame["Exec Time"])

    del data_frame["Exp"]
    del data_frame["Pos Effect"]
    del data_frame["Price"]
    del data_frame["Side"]
    del data_frame["Order Type"]
    del data_frame["Strike"]
    del data_frame["Spread"]
    data_frame.drop(
        data_frame.columns[data_frame.columns.str.contains("unnamed", case=False)],
        axis=1,
        inplace=True,
    )

    data_frame.to_csv(
        os.getcwd() + "/data/02_intermediate/01_df_trade_activity.csv",
        header=True,
        index=False,
    )


# TODO : implement switch case statement to return data specific to a type of import
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
