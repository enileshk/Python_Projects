import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    #path=r"C:\Users\inile\PyCharmMiscProject\epa-sea-level.csv.txt"
    path=r"epa-sea-level.csv"

    df=pd.read_csv(path)
    # Create scatter plot
    plt.scatter(df.Year, df['CSIRO Adjusted Sea Level'], color='blue', marker='o', label='Data points')
    #plt.show()

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_extended = np.arange(df["Year"].min(), 2051)
    sea_level_predicted = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_predicted, label="Line of Best Fit", color='red')
    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    slope_2000, intercept_2000, *_ = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = np.arange(2000, 2051)
    sea_level_predicted_2000 = slope_2000 * years_2000 + intercept_2000
    plt.plot(years_2000, sea_level_predicted_2000, label="Line of Best Fit", color='red')
    #plt.show()

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

