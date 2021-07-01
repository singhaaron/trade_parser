# main.py

# standard library
import sys, os

# pip packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# local modules
import d01_utils as stats
import d02_processing as preprocessor
import d04_visualization as vs


if __name__ == "__main__":

    # preprocess input
    preprocessor.frame_data(csv_path="/data/01_raw/01_trade_activity.csv", type="td")

    # process & output results
    preprocessor.process.analyze(
        csv_path="/data/02_intermediate/01_df_trade_activity.csv"
    )

    # analyze results
    df_trades = pd.read_csv(
        os.getcwd() + "/data/03_processed/01_df_trade_processed.csv"
    )

    # global vars
    tickers = df_trades["ticker"].values[::-1]
    profit_loss = df_trades["profit_loss"].values[::-1]
    capital_size = df_trades["cap"].values[::-1]
    time_duration = df_trades["time_duration"].values[::-1]
    entry_positions = df_trades["entry_pos"].values[::-1]
    exit_positions = df_trades["exit_pos"].values[::-1]

    # additional series
    total_sum = stats.cumulative_sum(profit_loss)
    total_sum_avg_10 = stats.cumulative_avg(profit_loss, avg=10)
    total_sum_avg_20 = stats.cumulative_avg(profit_loss, avg=20)

    # Set Matplotlib Plots
    plt.rcParams["figure.figsize"] = [9, 10]  # [width,length] unit = inches
    fig, axis = plt.subplots(nrows=3, ncols=2)
    fig2, axis2 = plt.subplots(nrows=3, ncols=1)
    fig3, axis3 = plt.subplots(nrows=3, ncols=1)

    # column_one: plot trends
    vs.plot_trend(axis[0][0], data=total_sum, title="Cumulative History")
    vs.plot_trend(axis[1][0], data=total_sum_avg_10, title="Avg Per 10 Trades")
    vs.plot_trend(axis[2][0], data=total_sum_avg_20, title="Avg Per 20 Trades")

    # column_two: plot trends w/color codes
    vs.color_coded_trend(axis[0][1], total_sum, title="Cumulative History")
    vs.color_coded_trend(axis[1][1], data=total_sum_avg_10, title="Avg Per 10 Trades")
    vs.color_coded_trend(axis[2][1], data=total_sum_avg_20, title="Avg Per 20 Trades")

    # scatter plot w/line of best fit
    vs.linear_regression_scatter_plot(
        axis=axis2[0],
        x=profit_loss,
        y=capital_size,
        xl="profit_loss",
        yl="cost_of_trade",
    )

    vs.linear_regression_scatter_plot(
        axis=axis2[1],
        x=range(len(time_duration)),
        y=np.true_divide(time_duration, 60),
        xl="trade_num",
        yl="minutes",
    )

    vs.linear_regression_scatter_plot(
        axis=axis2[2], x=capital_size, y=profit_loss, xl="trade_num", yl="profit_loss"
    )

    # bar charts
    vs.bar_chart(
        axis=axis3[0],
        x=range(len(profit_loss)),
        y=profit_loss,
        xl="trade_num",
        yl="profit_loss",
    )
    vs.bar_chart(
        axis=axis3[1],
        x=range(len(capital_size)),
        y=capital_size,
        xl="trade_num",
        yl="cost of trade",
    )
    vs.bar_chart(
        axis=axis3[2],
        x=range(len(time_duration)),
        y=np.true_divide(time_duration, 60),
        xl="trade_num",
        yl="minutes",
    )

    # histograms
    df_trades[df_trades.columns].hist(
        figsize=(10, 10),
        bins=16,
        grid=True,
        orientation="horizontal",
    )
    # plt.savefig("hist_01.png", bbox_inches="tight", dpi=100)

    # plot
    vs.vis_on(set=True)

    # save local
    # fig.savefig("trend_plots_01.png")
    # fig2.savefig("linear_regression_scatter_plots_01.png")
    # fig3.savefig("bar_charts_01.png")
