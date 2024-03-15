import pandas as pd
from sklearn.cluster import KMeans

# Load your dataset into a pandas DataFrame
# Replace 'your_dataset.csv' with the actual dataset file path
data = pd.read_csv('dod.csv')

# Select the columns you want to use for K-means clustering
# Replace 'column1' and 'column2' with the actual column names
selected_columns = data[['AGE', 'Cr']]

# Define the number of clusters (k)
k = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=k)
data['cluster'] = kmeans.fit_predict(selected_columns)

# Count the number of records in each cluster
cluster_counts = data['cluster'].value_counts()

# Save the cluster counts as a text file
with open('k.txt', 'w') as file:
    for cluster in cluster_counts.index:
        count = cluster_counts[cluster]
        file.write(f'Cluster {cluster}: {count} records\n')

print("K-means clustering completed, and cluster counts saved in k.txt")

