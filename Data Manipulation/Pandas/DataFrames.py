import pandas as pd

# Create a sample DataFrame
sample_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John Deo', 'Max Ruin', 'Arnold', 'Krish Star', 'John Mike',
             'Alex John', 'My John Rob', 'Asruid', 'Tes Qry', 'Big John'],
    'class': ['Four', 'Three', 'Three', 'Four', 'Four',
              'Four', 'Fifth', 'Five', 'Six', 'Four'],
    'mark': [75, 85, 55, 60, 60, 55, 78, 85, 78, 55],
})

# print the DataFrame
print(sample_data)

# Print a specific column
print(sample_data['name'])  # or print(sample_data.name)

# Print more than one column
print(sample_data[['name', 'mark']])

# Print the selected rows
print(sample_data[1:3])



# => loc and iloc (loc is label-based and iloc is integer position-based) - used to select rows from a DataFrame


# loc - label-based - print the row with label 2
print(sample_data.loc[2])

# iloc - integer position-based - print the row with index 2
print(sample_data.iloc[2])



# => loc and iloc also allow to select rows and columns

# print the name of the row with label 2, using loc
print(sample_data.loc[2, 'name'])
# print the name of the row with index 2, using iloc
print(sample_data.iloc[2, 1])

# print the name and mark of the rows with labels 2 and 3, using loc
print(sample_data.loc[[2, 3], ['name', 'mark']])
print(sample_data.iloc[[2, 3], [1, 3]])

# we can use : (slice) going from the beginning or to the end
print(sample_data.loc[: , ['name'] ])