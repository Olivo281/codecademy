import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample data
np.random.seed(42)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, size=len(x))
data = np.random.randn(1000)
category = np.random.choice(['A', 'B', 'C', 'D'], size=100)
values = np.random.rand(100)

# Set up the figure
fig, axs = plt.subplots(3, 3, figsize=(15, 12))

# 1. Line Plot - Best for showing trends over time
sns.lineplot(x=x, y=y, ax=axs[0, 0])
axs[0, 0].set_title('Line Plot')

# 2. Scatter Plot - Best for showing relationships between two variables
sns.scatterplot(x=x, y=y, color='r', alpha=0.5, ax=axs[0, 1])
axs[0, 1].set_title('Scatter Plot')

# 3. Histogram - Best for visualizing data distributions
sns.histplot(data, bins=30, kde=True, color='g', ax=axs[0, 2])
axs[0, 2].set_title('Histogram')

# 4. Box Plot - Best for detecting outliers and visualizing distribution
sns.boxplot(x=category, y=values, ax=axs[1, 0])
axs[1, 0].set_title('Box Plot')

# 5. Bar Chart - Best for categorical data comparison
sns.barplot(x=['A', 'B', 'C', 'D'], y=[10, 25, 15, 30], ax=axs[1, 1])
axs[1, 1].set_title('Bar Chart')

# 6. Heatmap - Best for visualizing correlation matrices or grid data
corr_matrix = np.corrcoef(np.random.randn(10, 10))
sns.heatmap(corr_matrix, ax=axs[1, 2], cmap='coolwarm', annot=True)
axs[1, 2].set_title('Heatmap')

# 7. Pie Chart - Best for showing proportions
axs[2, 0].pie([10, 25, 15, 30], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', colors=['r', 'g', 'b', 'y'])
axs[2, 0].set_title('Pie Chart')

# 8. Violin Plot - Best for comparing distributions
sns.violinplot(x=category, y=values, ax=axs[2, 1])
axs[2, 1].set_title('Violin Plot')

# 9. Area Chart - Similar to line plot but emphasizes volume
sns.lineplot(x=x, y=y, ax=axs[2, 2], color='purple', alpha=0.5)
axs[2, 2].fill_between(x, y, color='purple', alpha=0.3)
axs[2, 2].set_title('Area Chart')

plt.tight_layout()
plt.show()
