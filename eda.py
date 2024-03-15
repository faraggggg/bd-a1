import pandas as pd

# Load your dataset into a pandas DataFrame
data = pd.read_csv('dod.csv')  # Replace with your dataset file

# Perform EDA and generate insights
insights = []

# Insight 1: Calculate the mean of a numerical column
mean_value = data['AGE'].mean()
insights.append(f"Insight 1: The mean value of the 'AGE' is {mean_value:.2f}")

# Insight 2: Find the most common value in a categorical column
most_common_value = data['Gender'].mode().iloc[0]
insights.append(f"Insight 2: The most common value in 'Gender' is '{most_common_value}'")

# Insight 3: Calculate the correlation between two numerical columns
correlation = data['VLDL'].corr(data['LDL'])
insights.append(f"Insight 3: The correlation between 'VLDL' and 'LDL' is {correlation:.2f}")

# Save insights as text files
for i, insight in enumerate(insights, start=1):
    with open(f'eda-in-{i}.txt', 'w') as file:
        file.write(insight)

print("EDA insights saved as text files.")
