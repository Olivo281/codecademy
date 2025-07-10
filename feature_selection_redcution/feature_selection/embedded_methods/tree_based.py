import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer # Classification dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Install these if you haven't:
# pip install xgboost lightgbm catboost
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostClassifier, Pool

print("--- Feature Selection: Tree-based Models ---")

# 1. Load and Prepare Data
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print(f"Original dataset shape: {X.shape}")
print(f"Original features: {X.columns.tolist()}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Scaling is generally not strictly necessary for tree-based models,
# as they are not sensitive to feature scales, but it's good practice
# for consistency if you're comparing with other methods.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
X_train_scaled_df = pd.DataFrame(X_train_scaled, columns=X.columns) # Keep feature names
X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=X.columns)

# 2. Train various Tree-based Models and Extract Feature Importances

models = {
    "RandomForestClassifier": RandomForestClassifier(n_estimators=100, random_state=42),
    "GradientBoostingClassifier": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "LGBMClassifier": lgb.LGBMClassifier(random_state=42),
    "XGBClassifier": xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    "CatBoostClassifier": CatBoostClassifier(iterations=100, learning_rate=0.1, random_seed=42, verbose=0)
}

feature_importances_dict = {}

for name, model in models.items():
    print(f"\n--- Training {name} ---")
    if name == "CatBoostClassifier":
        # CatBoost has its own data wrapper for training
        train_pool = Pool(X_train_scaled_df, y_train)
        model.fit(train_pool, verbose=False)
    else:
        model.fit(X_train_scaled_df, y_train)

    # #TreeBasedExplanation: Feature importances are typically available via the `feature_importances_` attribute.
    # #TreeBasedExplanation: These scores indicate how much each feature contributes to the model's predictive power
    # #TreeBasedExplanation: (e.g., how much it reduces impurity in decision nodes).
    importances = model.feature_importances_
    feature_importances_dict[name] = pd.Series(importances, index=X.columns).sort_values(ascending=False)
    print(f"Top 5 Feature Importances for {name}:\n{feature_importances_dict[name].head(5)}")

# 3. Consolidate and Visualize Feature Importances
print("\n--- Consolidated Feature Importances (Top 10) ---")

# Create a DataFrame to hold all importances for comparison
all_importances_df = pd.DataFrame(feature_importances_dict)

# Select top N features based on, e.g., RandomForest importance
top_n = 10
rf_top_features = feature_importances_dict["RandomForestClassifier"].head(top_n).index.tolist()

# Plotting top importances from one model
plt.figure(figsize=(12, 8))
sns.barplot(x=feature_importances_dict["RandomForestClassifier"].head(top_n).values,
            y=feature_importances_dict["RandomForestClassifier"].head(top_n).index,
            palette='viridis')
plt.title(f'Top {top_n} Feature Importances from RandomForestClassifier')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
plt.show()

# 4. Use Selected Features for a Downstream Model
# #TreeBasedExplanation: After selecting features, you would retrain your chosen model
# #TreeBasedExplanation: (or a new one) using only the subset of selected features.
print(f"\n--- Example: Using Top {top_n} RandomForest Features ---")
X_train_selected = X_train_scaled_df[rf_top_features]
X_test_selected = X_test_scaled_df[rf_top_features]

# Train a classifier on the reduced feature set
final_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
final_classifier.fit(X_train_selected, y_train)

accuracy = final_classifier.score(X_test_selected, y_test)
print(f"Accuracy with top {top_n} features: {accuracy:.4f}")
print(f"New dataset shape: {X_train_selected.shape}")

print("\n--- Tree-based Models Feature Selection Complete ---")