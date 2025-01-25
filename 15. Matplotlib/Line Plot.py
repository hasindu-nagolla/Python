year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]
population = [2.5, 3.0, 3.7, 4.4, 5.3, 6.1, 6.9, 7.8, 8.5, 9.2, 9.7, 10.2, 10.8, 11.3, 11.8, 12.3]  # in billions

# Print the last item from year and population
print("Last year in the data:", year[-1])
print("Predicted population for 2100:", population[-1], "billion")

# Import matplotlib.pyplot as plt for data visualization
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, population on the y-axis
plt.plot(year, population)

# Set labels and title for clarity
plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.title('World Population Growth')

# Display the plot with plt.show()
plt.show()
 