# neural tradeazy

1.  Description
2.  Work In Progress
3.  Installation
4.  Directory Structure
5.  Contributions
6.  Dev Change Log

---
### i.Description

Project dedicated to mimicking [Tradervue](https://www.tradervue.com/), a trading journal to provide insights on trading activity but with more of a bang.

---
### ii. Work In Progress

- [x] Idea
- [x] Preprocessing Dataset
- [x] Data Visualization
- [ ] Training | Testing Models
    - [x] Linear Regression
    - [ ] Logistic Regression
    - [ ] Support Vector Machines (SVM)
    - [ ] Recurrent Neural Network (LSTM)
- [ ] UI for Presentation | Report

---
### iii.Installation

- Setup Enviornment `python3 -m venv virtual_environment`
- Activate Environment `source virtual_environment/bin/activate `
- Install Packages | Dependencies `pip install -r requirements.txt `
- Run Script from Root Directory ` python3 src/main.py`

---

### VI.Directory Structure

```bash
├── README.md #<-- README for developers using this project
├── data 
│   ├── 01_raw #<-- The original, immutable data dump
│   │   └── 01_trade_activity.csv
│   ├── 02_intermediate #<-- Intermediate data that has been transformed
│   │   └── 01_df_trade_activity.csv
│   ├── 03_processed #<-- The final, canonical data sets for modeling
│   │   ├── 01_df_trade_candles.csv
│   │   └── 01_df_trade_processed.csv
│   ├── 04_saved_models  #<-- Trained and serialized models, predictions, or summaries
│   │   └── multi_variant_linear_model.sav
│   └── 05_report #<-- Interface for presenting report
│       ├── 1.0-initial-data-exploration.html
│       ├── 2.0-linear_regression.html
│       ├── 2.0-logistic_regression.html
│       └── 2.0-lstm_neural_net.html
├── notebooks #<-- Jupyter Notebooks for Summary | Code executed in Segments
│   ├── 01_exploration
│   │   └── 1.0-initial-data-exploration.ipynb
│   └── 02_models
│       ├── 2.0-linear_regression.ipynb
│       ├── 2.0-logistic_regression.ipynb
│       └── 2.0-lstm_neural_net.ipynb
├── requirements.txt  #<-- Necessary installation packages for python virtual environment
└── src
    ├── d01_utils #<-- Functions used across the project
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── stats.cpython-39.pyc
    │   └── stats.py
    ├── d02_processing #<-- Scripts to turn intermediate data into modelling input
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   ├── preprocessor.cpython-39.pyc
    │   │   └── process.cpython-39.pyc
    │   ├── preprocessor.py
    │   └── process.py
    ├── d03_models #<-- Scripts to train models and then use trained models to make predictions
    │   ├── gradient_descent.py
    │   ├── mutli_linear_variant_regression.py
    │   ├── scratch_nerual_net.py
    │   └── train_model.py
    ├── d04_visualization #<--Scripts to create exploratory and results oriented visualizations
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-39.pyc
    │   │   └── vis.cpython-39.pyc
    │   └── vis.py
    └── main.py
```

---

### V. Contributions

|   Student Name   | GitHub Username |
| :--------------: | :-------------: |
|   Aaron Singh    |   singhaaron    |
| Andrei Georgescu |     Doxify      |

### VI.Dev Change Log
#### Monday, July 19, 2021

- models (multivariant linear regression)
- ui for current progress
- cleaned todo

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
