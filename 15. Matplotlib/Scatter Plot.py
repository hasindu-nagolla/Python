import matplotlib.pyplot as plt


gdp_cap = [15000, 2000, 7500, 50000, 3000, 60000, 22000, 10000, 4500, 8000,
           28000, 12000, 4000, 30000, 35000, 5000, 17000, 6000, 1000, 9000]

life_exp = [65, 55, 60, 78, 50, 82, 70, 68, 64, 62,
            75, 74, 59, 71, 80, 66, 73, 72, 67, 58]

# Change the line plot to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')  # study why putting the x-axis on a logarithmic scale.

# Set labels and title for clarity
plt.xlabel('GDP per Capital (log scale)')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy vs. GDP per Capita')

# Show plot
plt.show()
