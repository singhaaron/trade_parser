# process.py
import datetime
import os
import pandas as pd


def time_elapsed(start: datetime, end: datetime) -> int:
    """
    summary:
        take datetime object and return time elapsed from start to end of a position
    args:
        start: first element(time) of entry position
        end: last element(time) of exit position
    returns:
        pd.DataFrame: time duration from start to end of a postion
    """
    return end[-1].minute * 60 + end[-1].second - start[0].minute * 60 + start[0].second


def analyze(csv_path: str):
    """
    summary:
        return data frame w/condensed information and usable as a reflection of meaningful data
    args:
        df (pd.DataFrame): dataframe with proper formatted columns for type format
    returns:
        pd.DataFrame: dataframe with informated analyzed
    """

    df = pd.read_csv(os.getcwd() + csv_path, delimiter=",")
    open_trades = {}
    complete_trades = []
    target_columns = [
        "ticker",
        "profit_loss",
        "cap",
        "time_duration",
        "positions",
        "entry_pos",
        "exit_pos",
        "entrys",
        "exits",
    ]
    df["Exec Time"] = pd.to_datetime(df["Exec Time"])
    for index, row in df.iterrows():
        ticker = row["Symbol"]
        net_size = int(row["Qty"])
        net_position = row["Net Position"]
        net_cap = net_position if net_size > 0 else 0
        entrys = [row["Exec Time"]] if net_size > 0 else [0]
        exits = [row["Exec Time"]] if net_size < 0 else [0]
        if ticker in open_trades:
            open_trades[ticker]["net_size"] += net_size
            open_trades[ticker]["net_position"] += net_position
            open_trades[ticker]["net_cap"] += net_cap
            open_trades[ticker]["executions"]["entrys"] += entrys
            open_trades[ticker]["executions"]["exits"] += exits
            if True if open_trades[ticker]["net_size"] == 0 else False:
                entrys = [
                    _ for _ in open_trades[ticker]["executions"]["entrys"] if _ != 0
                ]
                exits = [
                    _ for _ in open_trades[ticker]["executions"]["exits"] if _ != 0
                ]
                complete_trades.append(
                    [
                        ticker,
                        -(round(open_trades[ticker]["net_position"], 2)),
                        round(open_trades[ticker]["net_cap"], 2),
                        time_elapsed(entrys, exits)
                        if time_elapsed(entrys, exits) > 0
                        and time_elapsed(entrys, exits) < 1800
                        else 0,
                        len(entrys) + len(exits),
                        len(entrys),
                        len(exits),
                        entrys,
                        exits,
                    ]
                )
                del open_trades[ticker]
        else:
            open_trades[ticker] = {
                "net_size": net_size,
                "net_position": net_position,
                "net_cap": net_cap,
                "executions": {"entrys": entrys, "exits": exits},
            }

    # turn list into dataframe
    df_churn = pd.DataFrame(
        data=complete_trades, index=range(len(complete_trades)), columns=target_columns
    )

    df_churn.to_csv(
        os.getcwd() + "/data/03_processed/01_df_trade_processed.csv",
        header=True,
    )
