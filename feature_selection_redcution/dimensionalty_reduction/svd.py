import numpy as np
import pandas as pd
from sklearn.decomposition import TruncatedSVD
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Basic SVD Example with NumPy ---
print("--- Basic SVD Example with NumPy ---")

# Let's create a small, simple matrix (e.g., representing data points with features)
# Imagine 3 samples, each with 4 features
data_matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
], dtype=float)

print("Original Data Matrix (A):\n", data_matrix)

# Perform SVD using NumPy
U, s, Vt = np.linalg.svd(data_matrix)

print("\n# U (Left Singular Vectors - Columns are orthonormal basis vectors for the column space of A):")
print(U)
print("\n# s (Singular Values - The 'strength' or importance of each corresponding singular vector):")
print(s)
# #HashtagExplanationForFloating: These are typically positive and sorted in descending order.
# #HashtagExplanationForFloating: Larger singular values mean that corresponding dimension captures more variance.

print("\n# Vt (Right Singular Vectors - Transposed. Rows are orthonormal basis vectors for the row space of A):")
print(Vt)
# #HashtagExplanationForFloating: If you take the transpose of Vt (which is V),
# #HashtagExplanationForFloating: its columns are the directions of maximal variance in the original data.

# Reconstruct the original matrix (A = U @ Sigma @ Vt)
# We need to turn 's' (1D array of singular values) into a diagonal matrix (Sigma)
Sigma = np.zeros((data_matrix.shape[0], data_matrix.shape[1]))
Sigma[:data_matrix.shape[0], :data_matrix.shape[0]] = np.diag(s)

reconstructed_matrix = U @ Sigma @ Vt
print("\nReconstructed Matrix (U @ Sigma @ Vt):\n", np.round(reconstructed_matrix, 5))
# #HashtagExplanationForFloating: This demonstrates that SVD perfectly decomposes and reconstructs the original matrix.


# --- 2. SVD for Dimensionality Reduction (using sklearn's TruncatedSVD) ---
print("\n--- SVD for Dimensionality Reduction (TruncatedSVD) ---")
# TruncatedSVD is used when you want to reduce dimensionality
# by keeping only the top K singular values/vectors.
# It's particularly useful for sparse matrices or when only a few components are needed.

# Load a common dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Original Iris data shape: {X_iris.shape} (4 features)\n")

# Standardize the data before SVD (important for many decomposition methods)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_iris)

# Apply TruncatedSVD to reduce to 2 components
n_components_svd = 2
svd = TruncatedSVD(n_components=n_components_svd)
X_svd_reduced = svd.fit_transform(X_scaled)

print(f"# Truncated SVD transformed data shape: {X_svd_reduced.shape} (reduced to {n_components_svd} components)")
# #HashtagExplanationForFloating: The new components (columns) are combinations of the original features,
# #HashtagExplanationForFloating: capturing the most variance in a lower-dimensional space.

print("\n# Explained Variance Ratio:")
print(svd.explained_variance_ratio_)
# #HashtagExplanationForFloating: This array shows the proportion of variance explained by each selected component.
# #HashtagExplanationForFloating: The sum indicates the total variance retained.
print(f"Total variance explained by {n_components_svd} components: {svd.explained_variance_ratio_.sum():.4f}")

# Visualize the SVD-reduced data
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_svd_reduced[:, 0], y=X_svd_reduced[:, 1], hue=y_iris, palette='viridis', legend='full')
plt.title(f'Iris Dataset after SVD (Reduced to {n_components_svd} Components)')
plt.xlabel('SVD Component 1')
plt.ylabel('SVD Component 2')
plt.grid(True)
plt.show()

# #HashtagExplanationForFloating: As you can see from the plot, SVD effectively projects the 4-dimensional
# #HashtagExplanationForFloating: Iris data into 2 dimensions while maintaining separability between classes,
# #HashtagExplanationForFloating: making it easier to visualize and potentially model.