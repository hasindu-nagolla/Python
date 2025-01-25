import os
import pandas as pd

# Create a sample DataFrame
sample_data = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John Deo', 'Max Ruin', 'Arnold', 'Krish Star', 'John Mike',
             'Alex John', 'My John Rob', 'Asruid', 'Tes Qry', 'Big John'],
    'class': ['Four', 'Three', 'Three', 'Four', 'Four',
              'Four', 'Fifth', 'Five', 'Six', 'Four'],
    'mark': [75, 85, 55, 60, 60, 55, 78, 85, 78, 55],
    'gender': ['female', 'male', 'male', 'female', 'female',
               'male', 'male', 'male', 'male', 'female']
})

# Save the file in the current directory (converting dataframe to csv)
sample_data.to_csv("test.csv", index=False)

# Now read it back and print
data = pd.read_csv("test.csv")
print(data)

# get the current working directory
print("Current working directory:", os.getcwd())
