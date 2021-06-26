import numpy as np
import vis
import preprocessor
import process

# path to csv
relative_path_data = "/sample_data/trade_activity.csv"

# preprocess csv to parse
orig_trade_csv = preprocessor.frame_data(
    csv_path=relative_path_data, type="TD Ameritrade"
)

# process csv
analzyed_csv = process.analyze(orig_trade_csv)

# dependent var Y:  Capital Size & independent var: X : P&L
vis.scatter_plot(
    np.array(analzyed_csv.loc[:, "p&l"]), np.array(analzyed_csv.loc[:, "cap"])
)

# Histograms of all Data Columns
vis.histogram(df_all=analzyed_csv)

# Linear Regression | Plot Relations
vis.linear_regression(
    x=np.array(analzyed_csv.loc[:, "p&l"]), y=np.array(analzyed_csv.loc[:, "cap"])
)
vis.linear_regression(
    x=np.array(analzyed_csv.loc[:, "p&l"]),
    y=np.array(analzyed_csv.loc[:, "time_duration"]),
)

# Plot Individual Column w/trade number(index)
vis.plot_line(df_all=analzyed_csv, y="cap", c="black")
vis.plot_line(df_all=analzyed_csv, y="p&l", c="black")

# Plot all Grids
vis.vis_on(set=True)
