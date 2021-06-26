import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# global plot config
# plt.style.use("dark_background")


def scatter_plot(x: np.array, y: np.array):
    plt.title("Scatter Plot")
    plt.grid(axis="x")
    plt.scatter(x, y, color="black")
    plt.xlabel("profit_loss")
    plt.ylabel("capital_size")
    plt.show()


def histogram(df_all: pd.DataFrame):
    plt.title("Histogram")
    df_all[["p&l", "cap", "time_duration", "entry pos", "exit pos"]].hist(
        figsize=(14, 9), bins=16, linewidth="1", edgecolor="k"
    )
    plt.show()


def linear_regression(x: np.array, y: np.array) -> plt.figure:
    plt.title("Linear Regression w/Scatter Plot")
    plt.xlabel("profit_loss")
    plt.ylabel("capital_size")
    plt.plot(x, y, "o")
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    plt.show()


def plot_line(df_all: pd.DataFrame, y: str, c: str):
    plt.grid(axis="y")
    df_all.plot(kind="line", y=y, use_index=True, color=c)
    plt.show()


def vis_on(set: bool):
    plt.show()
