import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression # To create a synthetic regression dataset

print("--- Feature Selection: Lasso Regression (L1 Regularization) ---")

# 1. Create a Synthetic Regression Dataset
# We'll create a dataset where some features are truly irrelevant (zero coefficient).
X, y, coef = make_regression(n_samples=1000, n_features=20, n_informative=5,
                             n_targets=1, noise=0.5, coef=True, random_state=42)
X = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
# True coefficients for informative features
true_coef_df = pd.DataFrame({'Feature': X.columns, 'True_Coefficient': coef})
true_informative_features = true_coef_df[true_coef_df['True_Coefficient'] != 0]['Feature'].tolist()

print(f"Original dataset shape: {X.shape}")
print(f"True number of informative features: {len(true_informative_features)}")
print(f"True informative features: {true_informative_features}")

# 2. Scale the Features (Important for regularization methods like Lasso)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns) # Keep feature names

# 3. Apply Lasso Regression for Feature Selection
# #LassoExplanation: Lasso adds an L1 penalty to the loss function. This penalty forces
# #LassoExplanation: the coefficients of less important features to become exactly zero.
# #LassoExplanation: 'alpha' controls the strength of the regularization. Higher alpha = more coefficients become zero.

# Try different alpha values
alpha_values = [0.01, 0.1, 1.0]

print("\n--- Lasso Coefficients for different alpha values ---")
for alpha in alpha_values:
    lasso = Lasso(alpha=alpha, random_state=42)
    lasso.fit(X_scaled_df, y)

    # Get coefficients
    coefficients = pd.Series(lasso.coef_, index=X_scaled_df.columns)

    # Count non-zero coefficients (selected features)
    selected_features = coefficients[coefficients != 0].index.tolist()
    num_selected_features = len(selected_features)

    print(f"\nAlpha = {alpha}:")
    print(f"  Number of selected features (non-zero coefficients): {num_selected_features}")
    print(f"  Selected features: {selected_features}")
    print(f"  Non-zero coefficients:\n{coefficients[coefficients != 0].sort_values(key=abs, ascending=False)}")

# To use Lasso for feature selection:
# Choose an alpha that yields a desired number of features or good model performance.
# Features with non-zero coefficients are the selected ones.
best_alpha = 0.1 # Example chosen alpha
final_lasso = Lasso(alpha=best_alpha, random_state=42)
final_lasso.fit(X_scaled_df, y)
final_selected_features = X_scaled_df.columns[final_lasso.coef_ != 0].tolist()

print(f"\n--- Final Selected Features with alpha={best_alpha} ---")
print(final_selected_features)
print(f"New dataset shape: {X_scaled_df[final_selected_features].shape}")

print("\n--- Lasso Regression Feature Selection Complete ---")