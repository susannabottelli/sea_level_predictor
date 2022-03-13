import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots()
    plt.scatter(x, y)
    

    # Create first line of best fit
    s = linregress(x,y)
    predx = pd.Series([p for p in range(1880, 2051)]) #remember to include year 2050 by ending the range at 2051
    predy = s.slope * predx + s.intercept
    plt.plot(predx, predy, "blue")

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    s2 = linregress(x2,y2)
    predx2 = pd.Series([p2 for p2 in range(2000, 2051)])
    predy2 = s2.slope * predx2 + s2.intercept
    plt.plot(predx2, predy2, "green")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()