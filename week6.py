# Working with pandas DataFrames
import numpy as np
import pandas as pd

# Create DataFrame from 2D array with custom row/column labels
data = np.array([['', 'Col1', 'Col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])

df1 = pd.DataFrame(data=data[1:, 1:], 
                   index=data[1:, 0], 
                   columns=data[0, 1:])
print("DataFrame from 2D array with labels:\n", df1)

# Create DataFrame from 2D array
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
df2 = pd.DataFrame(my_2darray)
print("\nDataFrame from 2D array:\n", df2)

# Create DataFrame from dictionary
my_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
df3 = pd.DataFrame(my_dict)
print("\nDataFrame from dictionary:\n", df3)

# Create DataFrame from another DataFrame
my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
df4 = pd.DataFrame(my_df)
print("\nDataFrame from another DataFrame:\n", df4)

# Create DataFrame from Series
my_series = pd.Series({
    "United Kingdom": "London",
    "India": "New Delhi",
    "United States": "Washington",
    "Belgium": "Brussels"
})
df5 = pd.DataFrame(my_series, columns=["Capital"])
print("\nDataFrame from Series:\n", df5)

# Using shape and index properties
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print("\nShape of the DataFrame:", df.shape)
print("Number of rows using len(df.index):", len(df.index))
