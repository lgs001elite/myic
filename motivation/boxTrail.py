import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Group': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C'],
    'Subgroup': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value': [1, 2, 1.5, 1.8, 3, 3.5, 2.9, 3.3, 4.5, 5.0, 4.3, 4.8]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='Value', hue='Subgroup', data=df, palette='Set2')

# Add a title
plt.title('Colored Boxplot', fontsize=16)

# Show the legend
plt.legend(title='Subgroup')

# Show the plot
plt.tight_layout()
plt.show()
