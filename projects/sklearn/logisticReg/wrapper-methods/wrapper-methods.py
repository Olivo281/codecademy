# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs

# Load the dataset
obesity = pd.read_csv("obesity.csv")

# Inspect the first few rows
print(obesity.head())

# Step 2: Split into predictors and outcome
X = obesity.drop(columns="NObeyesdad")
y = obesity["NObeyesdad"]

# Step 3: Create logistic regression model
lr = LogisticRegression(max_iter=1000)

# Step 4: Fit the model
lr.fit(X, y)

# Step 5: Evaluate model accuracy
full_accuracy = lr.score(X, y)
print("Full Feature Accuracy:", full_accuracy)

# --- Sequential Forward Selection (SFS) ---
sfs = SFS(lr,
          k_features=9,
          forward=True,
          floating=False,
          scoring='accuracy',
          cv=0)

sfs.fit(X, y)

# Step 8: Inspect selected features and accuracy
print("\nSequential Forward Selection Results:")
print(sfs.subsets_[9])
selected_features_sfs = sfs.subsets_[9]['feature_names']
sfs_accuracy = sfs.subsets_[9]['avg_score']
print("Selected features (SFS):", selected_features_sfs)
print("Accuracy with SFS:", sfs_accuracy)

# Step 10: Visualize SFS
plot_sfs(sfs.get_metric_dict())
plt.title('Sequential Forward Selection')
plt.grid()
plt.show()

# --- Sequential Backward Selection (SBS) ---
# Comment out SFS code above if runtime is an issue

sbs = SFS(lr,
          k_features=7,
          forward=False,
          floating=False,
          scoring='accuracy',
          cv=0)

sbs.fit(X, y)

# Step 13: Inspect selected features and accuracy
print("\nSequential Backward Selection Results:")
print(sbs.subsets_[7])
selected_features_sbs = sbs.subsets_[7]['feature_names']
sbs_accuracy = sbs.subsets_[7]['avg_score']
print("Selected features (SBS):", selected_features_sbs)
print("Accuracy with SBS:", sbs_accuracy)

# Step 15: Visualize SBS
plt.clf()
plot_sfs(sbs.get_metric_dict())
plt.title('Sequential Backward Selection')
plt.grid()
plt.show()

# --- Recursive Feature Elimination (RFE) ---
# Step 16: Save feature names
features = X.columns

# Step 17: Standardize X
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=features)

# Step 18: Create RFE object (selecting 8 features)
rfe = RFE(estimator=lr, n_features_to_select=8)

# Step 19: Fit RFE model
rfe.fit(X_scaled, y)

# Step 20: Get selected feature names
rfe_features = [feature for feature, keep in zip(features, rfe.support_) if keep]
print("\nRFE Selected Features:", rfe_features)

# Step 21: Evaluate RFE accuracy
rfe_accuracy = rfe.score(X_scaled, y)
print("Accuracy with RFE:", rfe_accuracy)

# Summary
print("\n--- Summary ---")
print(f"Accuracy with all features:     {full_accuracy:.4f}")
print(f"Accuracy with SFS (9 features): {sfs_accuracy:.4f}")
print(f"Accuracy with SBS (7 features): {sbs_accuracy:.4f}")
print(f"Accuracy with RFE (8 features): {rfe_accuracy:.4f}")
