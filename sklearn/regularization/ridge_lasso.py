import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate fake data
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 10)  # 10 features
true_coefs = np.array([5, -3, 0, 0, 2, 0, 0, 0, 1, 0])  # Sparse true coefficients
y = X @ true_coefs + np.random.randn(n_samples) * 2  # Add noise

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit Linear Regression (no regularization)
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_mse = mean_squared_error(y_test, lr_pred)

# Fit Ridge Regression
ridge = Ridge(alpha=10)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)
ridge_mse = mean_squared_error(y_test, ridge_pred)

# Fit Lasso Regression
lasso = Lasso(alpha=0.5)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)
lasso_mse = mean_squared_error(y_test, lasso_pred)

# Compare coefficients
coefs_df = pd.DataFrame({
    'True': true_coefs,
    'Linear': lr.coef_,
    'Ridge': ridge.coef_,
    'Lasso': lasso.coef_
})

# Print MSE
mse_results = {
    'Linear MSE': lr_mse,
    'Ridge MSE': ridge_mse,
    'Lasso MSE': lasso_mse
}

coefs_df, mse_results

#Making an array of C's; here we're choosing 100 values between 0.001 and 100
C_array  = np.logspace(-3,2, 100)

#Making a dict to enter as an input to param_grid
tuning_C = {'C':C_array}
clf = LogisticRegression(penalty = 'l1', solver =  'liblinear')
gs = GridSearchCV(clf, param_grid = tuning_C, scoring = 'accuracy', cv = 5)