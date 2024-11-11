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
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
