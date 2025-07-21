import numpy as np
from sklearn.datasets import make_regression, make_classification
from sklearn.linear_model import (
    LinearRegression, Ridge, Lasso, ElasticNet,
    RidgeCV, LassoCV, ElasticNetCV,
    LogisticRegression, LogisticRegressionCV,
    SGDRegressor, SGDClassifier,
    RANSACRegressor, HuberRegressor,
    Lars, LassoLars, OrthogonalMatchingPursuit,
    Perceptron, PassiveAggressiveClassifier, PassiveAggressiveRegressor,
    TweedieRegressor, QuantileRegressor, ARDRegression, BayesianRidge
)
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score

# ----------------- Regression Data ----------------- #
X_reg, y_reg = make_regression(n_samples=200, n_features=10, noise=10, random_state=0)
Xr_train, Xr_test, yr_train, yr_test = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

# ----------------- Classification Data ----------------- #
X_clf, y_clf = make_classification(n_samples=200, n_features=10, random_state=0)
Xc_train, Xc_test, yc_train, yc_test = train_test_split(X_clf, y_clf, test_size=0.3, random_state=42)

# ----------------- Regressors ----------------- #
print("Regressors:")

models_reg = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.1),
    "ElasticNet": ElasticNet(alpha=0.1, l1_ratio=0.5),
    "RidgeCV": RidgeCV(alphas=[0.1, 1.0, 10.0]),
    "LassoCV": LassoCV(cv=5),
    "ElasticNetCV": ElasticNetCV(cv=5),
    "SGDRegressor": SGDRegressor(max_iter=1000, tol=1e-3),
    "RANSACRegressor": RANSACRegressor(),
    "HuberRegressor": HuberRegressor(),
    "Lars": Lars(n_nonzero_coefs=5),
    "LassoLars": LassoLars(alpha=0.1),
    "OMP": OrthogonalMatchingPursuit(),
    "PassiveAggressiveRegressor": PassiveAggressiveRegressor(max_iter=1000),
    "TweedieRegressor": TweedieRegressor(power=0),
    "QuantileRegressor": QuantileRegressor(quantile=0.5),
    "ARDRegression": ARDRegression(),
    "BayesianRidge": BayesianRidge(),
}

for name, model in models_reg.items():
    try:
        model.fit(Xr_train, yr_train)
        score = r2_score(yr_test, model.predict(Xr_test))
        print(f"{name:30s}: R^2 = {score:.3f}")
    except Exception as e:
        print(f"{name:30s}: Failed ({e})")

# ----------------- Classifiers ----------------- #
print("\nClassifiers:")

models_clf = {
    "LogisticRegression": LogisticRegression(max_iter=500),
    "LogisticRegressionCV": LogisticRegressionCV(cv=5, max_iter=500),
    "SGDClassifier": SGDClassifier(max_iter=1000, tol=1e-3),
    "Perceptron": Perceptron(max_iter=1000),
    "PassiveAggressiveClassifier": PassiveAggressiveClassifier(max_iter=1000),
}

for name, model in models_clf.items():
    try:
        model.fit(Xc_train, yc_train)
        score = accuracy_score(yc_test, model.predict(Xc_test))
        print(f"{name:30s}: Accuracy = {score:.3f}")
    except Exception as e:
        print(f"{name:30s}: Failed ({e})")

#Making an array of C's; here we're choosing 100 values between 0.001 and 100
C_array  = np.logspace(-3,2, 100)

#Making a dict to enter as an input to param_grid
tuning_C = {'C':C_array}
clf = LogisticRegression(penalty = 'l1', solver =  'liblinear')
gs = GridSearchCV(clf, param_grid = tuning_C, scoring = 'accuracy', cv = 5)