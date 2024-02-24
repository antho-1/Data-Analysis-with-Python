import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv(r"C:\Users\antho\OneDrive\Education\FreeCodeCamp\Data Analysis with Python\Datasets\epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x = range(1880, 2051)  # Extend for prediction to 2050
    plt.plot(x, slope * x + intercept, label="All data")


    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    plt.plot(x, slope_2000 * x + intercept_2000, label="Since 2000")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    

    # Save plot and return data for testing
    plt.savefig(r"C:\Users\antho\OneDrive\Education\FreeCodeCamp\Data Analysis with Python\Figures\sea_level_plot.png")
    return plt.gca()

draw_plot()