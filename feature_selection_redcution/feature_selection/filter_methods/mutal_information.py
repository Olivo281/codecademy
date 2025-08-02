import pandas as pd
from sklearn.feature_selection import mutual_info_classif, mutual_info_regression, SelectKBest
from sklearn.datasets import load_breast_cancer, load_diabetes # Classification & Regression examples
from sklearn.preprocessing import StandardScaler

print("--- Feature Selection: Mutual Information ---")

# --- Example 1: Classification (Breast Cancer Dataset) ---
print("\n--- Mutual Information for Classification (Breast Cancer) ---")
data_clf = load_breast_cancer()
X_clf = pd.DataFrame(data_clf.data, columns=data_clf.feature_names)
y_clf = data_clf.target

# Scaling is good practice but not strictly required for Mutual Information as it's not distance-based.
# #MutualInformationExplanation: Mutual Information doesn't assume linearity or specific data distribution,
# #MutualInformationExplanation: making it very flexible. It requires non-negative features for `mutual_info_classif`
# #MutualInformationExplanation: if used with `SelectKBest`, but handles continuous features well.
scaler_clf = StandardScaler()
X_clf_scaled = scaler_clf.fit_transform(X_clf)
X_clf_scaled_df = pd.DataFrame(X_clf_scaled, columns=data_clf.feature_names) # Keep feature names

# Calculate Mutual Information scores for classification
mi_scores_clf = mutual_info_classif(X_clf_scaled_df, y_clf, random_state=42)

mi_df_clf = pd.DataFrame({'Feature': X_clf_scaled_df.columns, 'MI_Score': mi_scores_clf})
mi_df_clf = mi_df_clf.sort_values(by='MI_Score', ascending=False)

print("\nMutual Information Scores (Classification):")
print(mi_df_clf)

# Select top K features
k_features_to_select_clf = 10 # Example: select top 10 features

selector_clf = SelectKBest(mutual_info_classif, k=k_features_to_select_clf)
X_selected_clf = selector_clf.fit_transform(X_clf_scaled_df, y_clf)

selected_features_indices_clf = selector_clf.get_support(indices=True)
selected_feature_names_clf = X_clf_scaled_df.columns[selected_features_indices_clf].tolist()

print(f"\nTop {k_features_to_select_clf} features selected by Mutual Information (Classification):")
print(selected_feature_names_clf)
print(f"New dataset shape (Classification): {X_selected_clf.shape}")


# --- Example 2: Regression (Diabetes Dataset) ---
print("\n--- Mutual Information for Regression (Diabetes) ---")
data_reg = load_diabetes()
X_reg = pd.DataFrame(data_reg.data, columns=data_reg.feature_names)
y_reg = data_reg.target

scaler_reg = StandardScaler()
X_reg_scaled = scaler_reg.fit_transform(X_reg)
X_reg_scaled_df = pd.DataFrame(X_reg_scaled, columns=data_reg.feature_names) # Keep feature names

# Calculate Mutual Information scores for regression
mi_scores_reg = mutual_info_regression(X_reg_scaled_df, y_reg, random_state=42)

mi_df_reg = pd.DataFrame({'Feature': X_reg_scaled_df.columns, 'MI_Score': mi_scores_reg})
mi_df_reg = mi_df_reg.sort_values(by='MI_Score', ascending=False)

print("\nMutual Information Scores (Regression):")
print(mi_df_reg)

# Select top K features
k_features_to_select_reg = 5 # Example: select top 5 features

selector_reg = SelectKBest(mutual_info_regression, k=k_features_to_select_reg)
X_selected_reg = selector_reg.fit_transform(X_reg_scaled_df, y_reg)

selected_features_indices_reg = selector_reg.get_support(indices=True)
selected_feature_names_reg = X_reg_scaled_df.columns[selected_features_indices_reg].tolist()

print(f"\nTop {k_features_to_select_reg} features selected by Mutual Information (Regression):")
print(selected_feature_names_reg)
print(f"New dataset shape (Regression): {X_selected_reg.shape}")

print("\n--- Mutual Information Complete ---")