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
axs[0, 0].plot(x, y, label='Trend')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# 2. Scatter Plot - Best for showing relationships between two variables
axs[0, 1].scatter(x, y, c='r', alpha=0.5)
axs[0, 1].set_title('Scatter Plot')

# 3. Histogram - Best for visualizing data distributions
axs[0, 2].hist(data, bins=30, alpha=0.7, color='g')
axs[0, 2].set_title('Histogram')

# 4. Box Plot - Best for detecting outliers and visualizing distribution
sns.boxplot(x=category, y=values, ax=axs[1, 0])
axs[1, 0].set_title('Box Plot')

# 5. Bar Chart - Best for categorical data comparison
category_counts = [10, 25, 15, 30]
axs[1, 1].bar(['A', 'B', 'C', 'D'], category_counts, color='b')
axs[1, 1].set_title('Bar Chart')

# 6. Heatmap - Best for visualizing correlation matrices or grid data
corr_matrix = np.corrcoef(np.random.randn(10, 10))
sns.heatmap(corr_matrix, ax=axs[1, 2], cmap='coolwarm', annot=True)
axs[1, 2].set_title('Heatmap')

# 7. Pie Chart - Best for showing proportions
axs[2, 0].pie(category_counts, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', colors=['r', 'g', 'b', 'y'])
axs[2, 0].set_title('Pie Chart')

# 8. Violin Plot - Best for comparing distributions
sns.violinplot(x=category, y=values, ax=axs[2, 1])
axs[2, 1].set_title('Violin Plot')

# 9. Area Chart - Similar to line plot but emphasizes volume
axs[2, 2].fill_between(x, y, color='purple', alpha=0.5)
axs[2, 2].set_title('Area Chart')

plt.tight_layout()
plt.show()
