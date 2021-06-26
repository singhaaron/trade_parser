# process.py
import pandas as pd
import datetime


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


def analyze(df: pd.DataFrame) -> pd.DataFrame:
    """
    summary:
        return data frame w/condensed information and usable as a reflection of meaningful data
    args:
        df (pd.DataFrame): dataframe with proper formatted columns for type format
    returns:
        pd.DataFrame: dataframe with informated analyzed
    """
    open_trades = {}
    complete_trades = []
    target_columns = [
        "ticker",
        "p&l",
        "cap",
        "time_duration",
        "positions",
        "entry pos",
        "exit pos",
        "entrys",
        "exits",
    ]
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
                        time_elapsed(entrys, exits),
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
    return pd.DataFrame(complete_trades, columns=target_columns)
