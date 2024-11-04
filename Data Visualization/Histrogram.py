import matplotlib.pyplot as plt

# Life expectancy data for different countries in 2007
life_exp = [82, 80, 77, 75, 73, 70, 68, 66, 65, 63, 
            61, 60, 58, 57, 55, 54, 52, 50, 48, 45]

# Create a histogram of life expectancy, we only need one argument to create a histogram.
plt.hist(life_exp)

# we can also define bins like this
# plt.hist(life_exp, bins=5)  # study why we need bins and how it works.

## Display the histogram

# define the title and labels for axes
plt.title('Histogram of Life Expectancy in 2007')
plt.xlabel('Life Expectancy (years)')
plt.ylabel('Number of Countries')

# Display the plot
plt.show()

