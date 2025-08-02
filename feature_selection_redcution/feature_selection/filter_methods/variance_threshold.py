import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.datasets import make_classification # To create a sample dataset

print("--- Feature Selection: Variance Threshold ---")

# 1. Create a Synthetic Dataset for Demonstration
# We'll create a dataset where some features have very low variance.
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5,
                           n_redundant=0, n_repeated=0, n_clusters_per_class=1, random_state=42)
X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])

# Introduce low-variance features
X['low_var_1'] = 0.5 # Almost constant
X['low_var_2'] = [0 if i % 100 != 0 else 1 for i in range(1000)] # Very few 1s, mostly 0s
X['high_var_example'] = [i / 1000 for i in range(1000)] # Diverse values

print(f"Original dataset shape: {X.shape}")
print(f"Original features: {X.columns.tolist()}")

# Check variance of some features (for demonstration)
print("\nVariance of selected features (before thresholding):")
print(X[['low_var_1', 'low_var_2', 'high_var_example']].var())

# 2. Apply Variance Threshold
# #VarianceThresholdExplanation: Selects features with a variance greater than the specified threshold.
# #VarianceThresholdExplanation: Features with variance <= threshold are removed.
# #VarianceThresholdExplanation: Useful for removing features that are constant or almost constant.

# Set a threshold. Features with variance below this will be removed.
# A common starting point is 0, which removes only perfectly constant features.
# For this example, we'll pick a slightly higher threshold to demonstrate removal of low_var_1 and low_var_2.
threshold = 0.05 # Adjust this value to see its effect

selector = VarianceThreshold(threshold=threshold)
X_selected = selector.fit_transform(X)

# Get the names of the selected features
selected_features_indices = selector.get_support(indices=True)
selected_feature_names = X.columns[selected_features_indices].tolist()

print(f"\nFeatures selected (variance > {threshold}):")
print(selected_feature_names)
print(f"New dataset shape: {X_selected.shape}")

# Verify that low_var_1 and low_var_2 are likely removed if their variance is below the threshold
print("\nExample of removed features if below threshold:")
if 'low_var_1' not in selected_feature_names:
    print("- 'low_var_1' (its variance is very low, likely removed)")
if 'low_var_2' not in selected_feature_names:
    print("- 'low_var_2' (its variance is low, likely removed)")

print("\n--- Variance Threshold Complete ---")