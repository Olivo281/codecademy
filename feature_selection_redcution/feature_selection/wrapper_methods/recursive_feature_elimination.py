import pandas as pd
from sklearn.feature_selection import RFE, RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.datasets import load_breast_cancer # A good dataset for classification

print("--- Feature Selection: RFE (Recursive Feature Elimination) ---")

# 1. Load Dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print(f"Original dataset shape: {X.shape}")
print(f"Original features: {X.columns.tolist()}")

# 2. Choose an Estimator (Model)
# #RFEExplanation: RFE requires an estimator that has either a `coef_` attribute (like Linear models)
# #RFEExplanation: or a `feature_importances_` attribute (like Tree-based models).
estimator = LogisticRegression(max_iter=10000, random_state=42) # Increased max_iter for convergence

# --- Basic RFE (Selecting a fixed number of features) ---
# #RFEExplanation: `RFE` iteratively removes the least important features until only `n_features_to_select` remain.
n_features_to_select = 10 # Example: Select top 10 features

rfe_selector = RFE(estimator=estimator, n_features_to_select=n_features_to_select, step=1)
rfe_selector.fit(X, y)

selected_features_mask = rfe_selector.support_
selected_feature_names = X.columns[selected_features_mask].tolist()

print(f"\n--- RFE (Fixed n_features={n_features_to_select}) Results ---")
print(f"Selected features: {selected_feature_names}")
print(f"New dataset shape: {X.loc[:, selected_features_mask].shape}")

# --- RFE with Cross-Validation (RFECV - Finding optimal number of features) ---
# #RFEExplanation: `RFECV` performs RFE and then cross-validates different numbers of features
# #RFEExplanation: to find the optimal number of features that maximize the score.
print("\n--- RFECV (Finding Optimal Number of Features) Results ---")

# Using a more robust estimator for RFECV might be better
estimator_rfecv = RandomForestClassifier(n_estimators=100, random_state=42)

# Using StratifiedKFold for classification tasks
cv_strategy = StratifiedKFold(5) # 5-fold cross-validation

rfecv_selector = RFECV(estimator=estimator_rfecv, step=1, cv=cv_strategy, scoring='accuracy', n_jobs=-1)
rfecv_selector.fit(X, y)

optimal_features_mask = rfecv_selector.support_
optimal_feature_names = X.columns[optimal_features_mask].tolist()

print(f"Optimal number of features found by RFECV: {rfecv_selector.n_features_}")
print(f"Optimal features: {optimal_feature_names}")
print(f"New dataset shape: {X.loc[:, optimal_features_mask].shape}")
print(f"Best cross-validation score: {rfecv_selector.cv_results_['mean_test_score'][rfecv_selector.n_features_ - 1]:.4f}")

# Plot number of features vs. cross-validation score (helpful for RFECV)
plt.figure(figsize=(10, 6))
plt.title('RFECV: Number of Features vs. Cross-validation score')
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (accuracy)")
plt.plot(range(1, len(rfecv_selector.cv_results_['mean_test_score']) + 1), rfecv_selector.cv_results_['mean_test_score'])
plt.grid(True)
plt.show()

print("\n--- RFE Complete ---")