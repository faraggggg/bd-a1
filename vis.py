import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (replace with your own data)
data = ['HbA1c','Chol','TG','HDL']

# Create a bar plot using Seaborn
sns.barplot(x=range(len(data)), y=data)

# Add labels and title
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.title("Sample Bar Plot")

# Save the plot as "vis.png"
plt.savefig("vis.png")

# Show the plot (optional)
plt.show()