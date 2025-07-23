import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_digits
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

print("\n--- t-SNE Example (Iris & Digits Datasets) ---")

# --- Example 1: Iris Dataset (4 dimensions -> 2 dimensions) ---
print("\n# t-SNE on Iris Dataset:")
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
target_names_iris = iris.target_names

# #tSNEExplanation: Scaling is often recommended for t-SNE, though less critical than for PCA/LDA,
# #tSNEExplanation: as t-SNE is sensitive to scale differences.
scaler = StandardScaler()
X_iris_scaled = scaler.fit_transform(X_iris)

# #tSNEExplanation: n_components: The dimension of the embedded space (e.g., 2 for 2D plot).
# #tSNEExplanation: perplexity: Relates to the number of nearest neighbors to consider.
# #tSNEExplanation:              Adjusting this value is crucial for different datasets (typically 5-50).
# #tSNEExplanation:              Too low: many small clusters. Too high: points merge.
# #tSNEExplanation: n_iter: Number of iterations. Higher is better for convergence but slower.
# #tSNEExplanation: learning_rate: Controls the step size of the optimization.
# #tSNEExplanation: random_state: For reproducibility.

tsne_iris = TSNE(n_components=2, perplexity=30, n_iter=3000, learning_rate=200, random_state=42)
X_iris_tsne = tsne_iris.fit_transform(X_iris_scaled)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_iris_tsne[:, 0], y=X_iris_tsne[:, 1], hue=y_iris, palette='viridis', legend='full')
plt.title('Iris Dataset Visualization with t-SNE')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.grid(True)
plt.show()
# #tSNEExplanation: Notice how t-SNE effectively separates the three Iris classes into distinct clusters.


# --- Example 2: Digits Dataset (64 dimensions -> 2 dimensions) ---
# #tSNEExplanation: For higher-dimensional data, t-SNE can take longer.
# #tSNEExplanation: Often, it's beneficial to apply PCA first to reduce dimensionality to ~50-100 components
# #tSNEExplanation: before applying t-SNE, especially for very high-dimensional data.
print("\n# t-SNE on Digits Dataset (subset for speed):")
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

# Take a subset for faster demonstration
X_digits_subset, _, y_digits_subset, _ = train_test_split(X_digits, y_digits, test_size=0.8, random_state=42, stratify=y_digits)

scaler_digits = StandardScaler()
X_digits_subset_scaled = scaler_digits.fit_transform(X_digits_subset)

tsne_digits = TSNE(n_components=2, perplexity=30, n_iter=3000, learning_rate=200, random_state=42)
X_digits_tsne = tsne_digits.fit_transform(X_digits_subset_scaled)

plt.figure(figsize=(10, 8))
sns.scatterplot(x=X_digits_tsne[:, 0], y=X_digits_tsne[:, 1], hue=y_digits_subset, palette='tab10', legend='full', s=15)
plt.title('Digits Dataset Visualization with t-SNE (Subset)')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.legend(title='Digit', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
# #tSNEExplanation: You can see distinct clusters forming for different digits.
# #tSNEExplanation: Some digits (like 1 and 7) might overlap due to their visual similarity.