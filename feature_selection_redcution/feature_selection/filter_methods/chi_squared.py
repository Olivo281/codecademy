import pandas as pd
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_iris # Good for categorical target

print("--- Feature Selection: Chi-Squared Test ---")

# 1. Load and Prepare Data
# Iris has numerical features and a categorical target.
# For Chi-Squared, we need categorical features. We'll discretize some Iris features.
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Discretize numerical features to make them categorical for Chi-Squared
# We'll use pandas.cut for simple binning
X['sepal length (cm)_cat'] = pd.cut(X['sepal length (cm)'], bins=3, labels=['short', 'medium', 'long'])
X['sepal width (cm)_cat'] = pd.cut(X['sepal width (cm)'], bins=3, labels=['narrow', 'medium', 'wide'])
X['petal length (cm)_cat'] = pd.cut(X['petal length (cm)'], bins=3, labels=['small', 'mid', 'large'])
X['petal width (cm)_cat'] = pd.cut(X['petal width (cm)'], bins=3, labels=['tiny', 'avg', 'broad'])

# Drop original numerical features and keep only the new categorical ones
X_categorical = X.drop(columns=data.feature_names)

# Chi-squared requires non-negative features. Label encode categorical features.
# #ChiSquaredExplanation: Chi-squared test works with non-negative features.
# #ChiSquaredExplanation: For categorical features, label encoding converts them to integers (non-negative).
X_encoded = X_categorical.apply(LabelEncoder().fit_transform)

print(f"Original categorical features: {X_encoded.columns.tolist()}")

# 2. Apply Chi-Squared Test
# #ChiSquaredExplanation: `chi2` returns F-scores and p-values for each feature.
# #ChiSquaredExplanation: Higher F-score (and lower p-value) indicates stronger dependence on the target.
# #ChiSquaredExplanation: `SelectKBest` then selects the top K features based on these scores.

# Calculate chi-squared scores
chi_scores, p_values = chi2(X_encoded, y)

chi_df = pd.DataFrame({'Feature': X_encoded.columns, 'Chi2_Score': chi_scores, 'P_Value': p_values})
chi_df = chi_df.sort_values(by='Chi2_Score', ascending=False)

print("\n--- Chi-Squared Scores for Categorical Features ---")
print(chi_df)

# Select top K features based on Chi-Squared score
k_features_to_select = 2 # Example: select top 2 features

selector = SelectKBest(chi2, k=k_features_to_select)
X_selected_chi2 = selector.fit_transform(X_encoded, y)

selected_features_indices = selector.get_support(indices=True)
selected_feature_names = X_encoded.columns[selected_features_indices].tolist()

print(f"\nTop {k_features_to_select} features selected by Chi-Squared:")
print(selected_feature_names)
print(f"New dataset shape: {X_selected_chi2.shape}")

print("\n--- Chi-Squared Test Complete ---")