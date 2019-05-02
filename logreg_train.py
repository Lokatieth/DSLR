import matplotlib.pyplot as plt;
import pandas as pd;
import numpy as np
import math;
import csv;
import sys;

DATA_SET_PATH = "./resources/dataset_train.csv"


def main():
    """
    Logistic Regression classifier main
    :return:
    """
    # Load the data set for training and testing the logistic regression classifier
    dataset = pd.read_csv(DATA_SET_PATH)
    print (dataset['Hogwarts House'].unique())

    

if __name__ == "__main__":
    main()