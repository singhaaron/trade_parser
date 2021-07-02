# neural tradeazy

---

1.  Description
2.  Installation
3.  Directory Structure
4.  Work In Progress
5.  Contributions
6.  Dev Change Log

### i.Description

---

Project dedicated to mimicking [Tradervue](https://www.tradervue.com/), a trading journal to provide insights on trading activity but with more of a bang.

Methods involved:

- Descriptive | Inferential Statistics
- Data Visualization
- Machine Learning
- Predictive Modeling

### ii.Installation

- Setup Enviornment `python3 -m venv virtual_environment`
- Activate Environment `source virtual_environment/bin/activate `
- Install Packages | Dependencies `pip install -r requirements.txt `
- Run Script from Root Directory ` python3 src/main.py`

---

### iii.Directory Structure

```bash
├── README.md #<--README for developers using this project
├── data
│   ├── 01_raw #<-- The original, immutable data dump
│   │   └── 01_trade_activity.csv
│   ├── 02_intermediate  #<-- Intermediate data that has been transformed.
│   │   └── 01_df_trade_activity.csv
│   ├── 03_processed #<--The final, canonical data sets for modeling
│   │   └── 01_df_trade_processed.csv
│   ├── 04_model #<-- Trained and serialized models, model predictions, or model summaries
│   └── 05_report
├── notebooks #<-- Jupyter notebook
│   └── 01_exploration
│       ├── 1.0-aaron-initial-data-exploration.ipynb
│       ├── bar_charts_01.png
│       ├── hist_01.png
│       ├── linear_regression_scatter_plots_01.png
│       └── trend_plots_01.png
├── requirements.txt #<-- Necessary installation packages for python virtual environment
└── src
    ├── d01_utils #<-- Functions used across the project
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── stats.cpython-39.pyc
    │   └── stats.py
    ├── d02_processing #<-- Scripts to turn intermediate data into modelling input
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── preprocessor.cpython-39.pyc
    │   │   └── process.cpython-39.pyc
    │   ├── preprocessor.py
    │   └── process.py
    ├── d03_models #<-- Scripts to train models and then use trained models to make predictions
    ├── d04_visualization #<--Scripts to create exploratory and results oriented visualizations
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── vis.cpython-39.pyc
    │   └── vis.py
    └── main.py
```

---

### IV. Work In Progress

- [x] Idea
- [x] Preprocessing Data
- [ ] Descriptive | Inferential Statistic Report
- [ ] Machine Learning (Training Model w/ Tensorflow & Scartch_Neural_Net)
- [ ] Predictive Modeling(Trained Model)
- [ ] Data Visualization
- [ ] UI | Server

### V. Contributions

|   Student Name   | GitHub Username |
| :--------------: | :-------------: |
|   Aaron Singh    |   singhaaron    |
| Andrei Georgescu |     Doxify      |

### VI.Dev Change Log

#### Thursday, July 1, 2021

- intial data exploration details preprocessed data before modeling

#### Wenesday, June 30, 2021

- revamped dir structure to a from a [template github repo](https://github.com/mishaberrien/standardize-py) for ml related projects

#### Tuesday, June 29, 2021

- docstring annotations
- summary jupyter notebook clean

#### Friday, June 25, 2021

- visuals
- module seperation

#### Wenesday, June 23, 2021

- init
