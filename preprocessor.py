import pandas as pd
import numpy as np
import os


def frame_data(csv_path: str, type: str) -> pd.DataFrame:
    data_frame = pd.read_csv(os.getcwd() + csv_path, delimiter=",")
    data_frame["Net Position"] = np.where(
        data_frame["Spread"] == "STOCK",
        data_frame["Qty"] * data_frame["Net Price"],
        data_frame["Qty"] * data_frame["Net Price"] * 100,
    )
    data_frame["Exec Time"] = pd.to_datetime(data_frame["Exec Time"])
    return data_frame
