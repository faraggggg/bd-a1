import pandas as pd

# Replace 'your_dataset.csv' with the actual file path of your CSV dataset
file_path = 'dod.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Now you can work with the 'df' DataFrame
# For example, you can print the first 5 rows of the DataFrame
print(df.head())