import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, load_digits
from sklearn.preprocessing import StandardScaler
import umap # UMAP library

print("\n--- UMAP Example (Iris & Digits Datasets) ---")

# --- Example 1: Iris Dataset (4 dimensions -> 2 dimensions) ---
print("\n# UMAP on Iris Dataset:")
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
target_names_iris = iris.target_names

scaler = StandardScaler()
X_iris_scaled = scaler.fit_transform(X_iris)

# #UMAPExplanation: n_components: The dimension of the embedded space.
# #UMAPExplanation: n_neighbors: Controls how UMAP balances local vs. global structure.
# #UMAPExplanation:              Small values (e.g., 2-10) emphasize local structure (like t-SNE).
# #UMAPExplanation:              Large values (e.g., 50-200) emphasize global structure.
# #UMAPExplanation: min_dist: Controls how tightly packed points are allowed to be in the low-dimensional space.
# #UMAPExplanation:           Small values (e.g., 0.0) allow points to be very close.
# #UMAPExplanation:           Large values (e.g., 0.5) prevent points from collapsing on top of each other.
# #UMAPExplanation: random_state: For reproducibility.

reducer_iris = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.1, random_state=42)
X_iris_umap = reducer_iris.fit_transform(X_iris_scaled)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_iris_umap[:, 0], y=X_iris_umap[:, 1], hue=y_iris, palette='viridis', legend='full')
plt.title('Iris Dataset Visualization with UMAP')
plt.xlabel('UMAP Component 1')
plt.ylabel('UMAP Component 2')
plt.grid(True)
plt.show()
# #UMAPExplanation: UMAP also effectively separates the Iris classes. Often, the separation is cleaner than t-SNE
# #UMAPExplanation: and the overall cluster shapes might better reflect global distances.


# --- Example 2: Digits Dataset (64 dimensions -> 2 dimensions) ---
print("\n# UMAP on Digits Dataset (subset for speed):")
digits = load_digits()
X_digits = digits.data
y_digits = digits.target

# Take a subset for faster demonstration
X_digits_subset, _, y_digits_subset, _ = train_test_split(X_digits, y_digits, test_size=0.8, random_state=42, stratify=y_digits)

scaler_digits = StandardScaler()
X_digits_subset_scaled = scaler_digits.fit_transform(X_digits_subset)

reducer_digits = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.1, random_state=42)
X_digits_umap = reducer_digits.fit_transform(X_digits_subset_scaled)

plt.figure(figsize=(10, 8))
sns.scatterplot(x=X_digits_umap[:, 0], y=X_digits_umap[:, 1], hue=y_digits_subset, palette='tab10', legend='full', s=15)
plt.title('Digits Dataset Visualization with UMAP (Subset)')
plt.xlabel('UMAP Component 1')
plt.ylabel('UMAP Component 2')
plt.legend(title='Digit', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()
# #UMAPExplanation: UMAP often produces more visually coherent clusters and preserves more of the global
# #UMAPExplanation: structure (how clusters relate to each other) compared to t-SNE, and it's generally faster.