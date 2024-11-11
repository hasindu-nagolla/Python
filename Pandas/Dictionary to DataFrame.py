# Using Pandas, we can convert a dictionary to a DataFrame.

import pandas as pd

# Create three lists for store the data
names = ['United States', 'Australia', 'Japan',
         'India', 'Russia', 'Morocco', 'Egypt']
driveSide = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create a dictionary with the data (lists)
data = {'Country Name': names, 'Drive Side': driveSide, 'Cars Per Capita': cpc}

# Create a DataFrame from the dictionary
cars_DataFrame = pd.DataFrame(data)

# Print the DataFrame
print(cars_DataFrame)



# Specify the index (row labels) for the DataFrame

# Create a list with the row labels
rowLabels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Create a DataFrame from the dictionary with the row labels
cars_DataFrame = pd.DataFrame(data, index=rowLabels) # or cars_DataFrame.index = rowLabels
 
# Print the DataFrame
print(cars_DataFrame)
