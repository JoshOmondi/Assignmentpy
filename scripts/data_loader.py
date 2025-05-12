import pandas as pd
import numpy as np

# Function to load CSV
def load_csv(filepath='data/sample.csv'):  # Default to 'data/sample.csv' in case no argument is passed
    return pd.read_csv(filepath)

# Function to load Excel (if needed, replace with the actual path to the Excel file)
def load_excel(filepath='data/sample.xlsx'):  # Change to an actual Excel file path if you have one
    return pd.read_excel(filepath)

# Function to load JSON (if you have a JSON file)
def load_json(filepath='data/sample.json'):  # Replace with a valid JSON file path if available
    return pd.read_json(filepath)

# Function to load NumPy (numerical data)
def load_numpy(filepath='data/sample.csv', delimiter=","):
    return np.loadtxt(filepath, delimiter=delimiter)  # Reads a .csv as a numpy array
