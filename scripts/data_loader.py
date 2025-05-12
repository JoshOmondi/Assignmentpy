import pandas as pd
import numpy as np

def load_csv(filepath):
    return pd.read_csv(filepath)

def load_excel(filepath):
    return pd.read_excel(filepath)

def load_json(filepath):
    return pd.read_json(filepath)

def load_numpy(filepath, delimiter=","):
    return np.loadtxt(filepath, delimiter=delimiter)
