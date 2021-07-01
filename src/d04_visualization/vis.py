# vis.py
import matplotlib.pyplot as plt
import numpy as np


def linear_regression_scatter_plot(
    axis: np.ndarray, x: np.array, y: np.array, xl: str, yl: str
):
    axis.set_xlabel(xl)
    axis.set_ylabel(yl)
    axis.plot(x, y, "o")
    m, b = np.polyfit(x, y, 1)
    axis.plot(x, m * x + b)


def plot_trend(axis: np.ndarray, data: list[float], title: str):
    axis.plot(range(len(data)), data)
    axis.set_title(title)
    axis.grid()


def bar_chart(axis: np.ndarray, x: list[float], y: list[float], xl: str, yl: str):
    axis.bar(x, y)
    axis.set_xlabel(xl)
    axis.set_ylabel(yl)


def color_coded_trend(axis: np.ndarray, data: list[float], title: str):
    y_axis, x_axis = data, range(len(data))
    for x1, x2, y1, y2 in zip(x_axis, x_axis[1:], y_axis, y_axis[1:]):
        if y1 > y2:
            axis.plot([x1, x2], [y1, y2], "r")
        elif y1 < y2:
            axis.plot([x1, x2], [y1, y2], "g")
        else:
            axis.plot([x1, x2], [y1, y2], "y")
        axis.set_title(title)
    axis.grid()


def vis_on(set: bool):
    plt.tight_layout()
    plt.show()
