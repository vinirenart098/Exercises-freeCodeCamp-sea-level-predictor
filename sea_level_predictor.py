import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    line1 = [slope * year + intercept for year in years]
    plt.plot(years, line1, color='red', label='Best Fit Line (1880-2050)')

    # Create second line of best fit using data from year 2000
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    line2 = [slope_recent * year + intercept_recent for year in years_recent]
    plt.plot(years_recent, line2, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY) - do not modify the test module
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Call the function to draw the plot
draw_plot()
