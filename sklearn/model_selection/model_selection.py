import numpy as np
from sklearn.datasets import load_iris, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (
    train_test_split, KFold, StratifiedKFold, GroupKFold, cross_val_score,
    cross_validate, GridSearchCV, RandomizedSearchCV,
    ShuffleSplit, StratifiedShuffleSplit,
    LeaveOneOut, LeavePOut, GroupShuffleSplit,
    learning_curve, validation_curve
)
from sklearn.metrics import accuracy_score
from scipy.stats import uniform

# ----------------- Load Dataset ----------------- #
X, y = load_iris(return_X_y=True)

# ----------------- train_test_split ----------------- #
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----------------- Cross-Validation ----------------- #
clf = LogisticRegression(max_iter=500)

# Basic KFold
kf = KFold(n_splits=5)
print("KFold scores:", cross_val_score(clf, X, y, cv=kf))

# StratifiedKFold
skf = StratifiedKFold(n_splits=5)
print("StratifiedKFold scores:", cross_val_score(clf, X, y, cv=skf))

# ShuffleSplit
ss = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
print("ShuffleSplit scores:", cross_val_score(clf, X, y, cv=ss))

# LeaveOneOut
loo = LeaveOneOut()
loo_scores = cross_val_score(clf, X[:10], y[:10], cv=loo)
print("LeaveOneOut scores (first 10 samples):", loo_scores)

# LeavePOut (p=2)
lpo = LeavePOut(p=2)
lpo_scores = cross_val_score(clf, X[:10], y[:10], cv=lpo)
print("LeavePOut scores (first 10 samples):", lpo_scores[:5], "...")

# ----------------- GroupKFold & GroupShuffleSplit ----------------- #
X_grp, y_grp = make_classification(n_samples=100, n_features=4, random_state=42)
groups = np.random.randint(0, 10, size=100)

gkf = GroupKFold(n_splits=5)
print("GroupKFold scores:", cross_val_score(clf, X_grp, y_grp, groups=groups, cv=gkf))

gss = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
print("GroupShuffleSplit scores:", cross_val_score(clf, X_grp, y_grp, groups=groups, cv=gss))

# ----------------- cross_validate ----------------- #
scoring = ['accuracy', 'f1_macro']
cv_results = cross_validate(clf, X, y, cv=5, scoring=scoring, return_train_score=True)
print("cross_validate results:\n", cv_results)

# ----------------- GridSearchCV ----------------- #
param_grid = {'C': [0.01, 0.1, 1, 10]}
grid = GridSearchCV(clf, param_grid, cv=5)
grid.fit(X, y)
print("GridSearchCV best params:", grid.best_params_)

# ----------------- RandomizedSearchCV ----------------- #
param_dist = {'C': uniform(loc=0.01, scale=10)}
random_search = RandomizedSearchCV(clf, param_distributions=param_dist, n_iter=10, cv=5, random_state=42)
random_search.fit(X, y)
print("RandomizedSearchCV best params:", random_search.best_params_)

# ----------------- Learning Curve ----------------- #
train_sizes, train_scores, test_scores = learning_curve(clf, X, y, cv=5)
print("Learning Curve Train Sizes:", train_sizes)

# ----------------- Validation Curve ----------------- #
param_range = np.logspace(-3, 2, 5)
train_scores, test_scores = validation_curve(clf, X, y, param_name="C", param_range=param_range, cv=5)
print("Validation Curve for 'C':", param_range)
