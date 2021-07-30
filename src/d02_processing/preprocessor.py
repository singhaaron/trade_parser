# preprocessor.py

# standard library
import os
import pprint as pp

# pip packages
import pandas as pd
import numpy as np

# web scraping
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen

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

def ticker_metrics(csv_path: str):
    """
    summary:
        scrape finviz for symbol's metrics
    args:
        csv_path (str): local path to trade history
    returns:
        writes | updates ticker metrics to csv on disk
    """
    read_from_disk_loc = os.getcwd() + csv_path
    write_to_disk_loc = os.getcwd()+'/data/02_intermediate/01_ticker_metrics_table.csv'
    df = pd.read_csv(read_from_disk_loc,delimiter=",",error_bad_lines=False,)
    symbols = set(df['Symbol'].unique())
    if os.path.exists(write_to_disk_loc):
        df_metrics_table = pd.read_csv(write_to_disk_loc,index_col=0,error_bad_lines=False)
        symbols_read = set(df_metrics_table.index)
        symbols = symbols.difference(symbols_read)
    print('running fetch for follow tickers',symbols)
    if len(symbols) == 0:
        return
    metrics_table = dict()
    for s in symbols:
        try:
            s_metrics = dict()
            url = "http://finviz.com/quote.ashx?t=" + s.lower()
            req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            webpage = urlopen(req).read()
            html = soup(webpage, "html.parser")
            t_m = pd.read_html(str(html), attrs={"class": "snapshot-table2"})[0]
            for i,r in t_m.iterrows():
                [s_metrics.update({r[_]:r[_+1]}) for _ in np.arange(0,12,2) ]
            metrics_table.update({s:s_metrics})
        except Exception as e:
            # metrics_table.update({s:None})
            print('prolly soup error',e)
    init_metrics_table = pd.DataFrame.from_dict(metrics_table,orient='index')
    init_metrics_table.replace(r'^\s*$', np.nan, regex=True)
    if os.path.exists(write_to_disk_loc):
        try:
            init_metrics_table.to_csv(write_to_disk_loc, mode='a', header=False)
        except Exception as e:
            print('some error in appending',e)
    else:
        init_metrics_table.to_csv(write_to_disk_loc)

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
