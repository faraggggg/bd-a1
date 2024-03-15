import pandas as pd
import numpy as np  # Import the numpy library
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import KBinsDiscretizer

# Load your dataset into a pandas DataFrame
data = pd.read_csv('dod.csv')

# Data Cleaning:
# Task 1: Handling Missing Values - Replace missing values with the mean of the respective column
data.fillna(data.mean(), inplace=True)

# Task 2: Removing Outliers - Detect and remove outliers using z-scores
z_scores = (data - data.mean()) / data.std()
outliers = (z_scores > 3).any(axis=1)
data_cleaned = data[~outliers]

# Data Transformation:
# Task 3: Log Transformation - Apply a logarithmic transformation to specific columns
log_transform_columns = ['column1', 'column2']
data_cleaned[log_transform_columns] = data_cleaned[log_transform_columns].apply(lambda x: np.log(x))

# Task 4: Label Encoding - Convert categorical variables to numerical labels using label encoding
label_encoder = LabelEncoder()
data_cleaned['categorical_column'] = label_encoder.fit_transform(data_cleaned['categorical_column'])

# Data Reduction:
# Task 5: Feature Selection - Select the most important features using SelectKBest
selector = SelectKBest(score_func=f_classif, k=3)
selected_features = selector.fit_transform(data_cleaned[['feature1', 'feature2', 'feature3', 'categorical_column']], data_cleaned['target'])

# Task 6: Dimensionality Reduction - Apply Principal Component Analysis (PCA)
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(selected_features)

# Data Discretization:
# Task 7: Custom Binning - Define custom bin edges to discretize a numerical feature
bin_edges = [0, 100, 200, 300, 400, 500]
data_cleaned['custom_binned_feature'] = pd.cut(data_cleaned['numeric_feature'], bins
=bin_edges)

# Task 8: Quantile-Based Discretization - Use quantiles to create bins
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')
discretized_data = discretizer.fit_transform(reduced_data)

# Create a new DataFrame with the processed data
processed_df = pd.DataFrame(data=discretized_data, columns=['Feature1', 'Feature2'])

# Save the resulting data frame as a new CSV file

print("Data cleaning, transformation, reduction, and discretization steps are completed. Processed data saved as res_dpre.csv")
# Assuming you have a DataFrame named 'result_df' that you want to save

# Code to create or manipulate your DataFrame goes here

result_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
result_df.to_csv('res_dpre.csv', index=False)


# The 'index=False' parameter ensures that the index column is not saved in the CSV file
