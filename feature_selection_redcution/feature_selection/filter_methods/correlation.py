import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer # A good dataset with numerical features

print("--- Feature Selection: Correlation ---")

# 1. Load Dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

print(f"Original dataset shape: {X.shape}")
print(f"Original features: {X.columns.tolist()}")

# 2. Feature-Target Correlation (Selecting relevant features)
# #CorrelationExplanation: Calculate the correlation between each feature and the target variable.
# #CorrelationExplanation: Features with higher absolute correlation values are generally more relevant.
feature_target_correlations = X.corrwith(y).abs().sort_values(ascending=False)

print("\n--- Feature-Target Correlation (Absolute Values) ---")
print(feature_target_correlations)

# Define a threshold for selecting features highly correlated with the target
target_corr_threshold = 0.5 # Example threshold

selected_by_target_corr = feature_target_correlations[feature_target_correlations > target_corr_threshold].index.tolist()
print(f"\nFeatures selected based on target correlation (>{target_corr_threshold}):")
print(selected_by_target_corr)

# 3. Feature-Feature Correlation (Removing redundant features)
# #CorrelationExplanation: Calculate the correlation matrix among features.
# #CorrelationExplanation: Identify pairs of features that are highly correlated with each other.
# #CorrelationExplanation: Remove one from each pair to reduce redundancy (multicollinearity).

correlation_matrix = X.corr().abs() # Absolute correlation for magnitude
# Fill diagonal with 0s to avoid self-correlation, and upper triangle for unique pairs
np.fill_diagonal(correlation_matrix.values, 0) # Set diagonal to 0
upper_tri = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))

# Visualize the correlation matrix (optional but highly recommended)
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=False, cmap='viridis', fmt=".2f",
            xticklabels=X.columns, yticklabels=X.columns)
plt.title('Absolute Feature-Feature Correlation Matrix')
plt.show()

# Define a threshold for highly correlated features to remove
feature_feature_corr_threshold = 0.9 # Example threshold for very high correlation

# Find features to drop
features_to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > feature_feature_corr_threshold)]

print(f"\n--- Features to Drop (highly correlated with other features, >{feature_feature_corr_threshold}) ---")
if features_to_drop:
    print(features_to_drop)
    X_reduced_by_feature_corr = X.drop(columns=features_to_drop)
    print(f"New dataset shape after dropping highly correlated features: {X_reduced_by_feature_corr.shape}")
else:
    print("No features found to drop based on the set threshold.")
    X_reduced_by_feature_corr = X.copy() # No change

print("\n--- Correlation Feature Selection Complete ---")