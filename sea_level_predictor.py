import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.6, label='Original Data')

    # 3. Create first line of best fit (all available data through year 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series(range(df['Year'].min(), 2051))
    sea_level_all = res_all.slope * years_all + res_all.intercept
    ax.plot(years_all, sea_level_all, color='red', label='Fit: 1880-2050')

    # 4. Create second line of best fit (data from year 2000 through 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = res_recent.slope * years_recent + res_recent.intercept
    ax.plot(years_recent, sea_level_recent, color='green', label='Fit: 2000-2050')

    # 5. Add labels, title, and adjust axes
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()