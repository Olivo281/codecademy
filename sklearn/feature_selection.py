import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.feature_selection import (
    SelectKBest, SelectPercentile, chi2, f_classif, mutual_info_classif,
    GenericUnivariateSelect, VarianceThreshold,
    RFE, RFECV, SelectFromModel
)
from sklearn.linear_model import LogisticRegression, Lasso
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

# Generate synthetic classification dataset
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
feature_names = [f'feature_{i}' for i in range(X.shape[1])]
df = pd.DataFrame(X, columns=feature_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# ----------------------------
# 1. Filter Methods
# ----------------------------

# SelectKBest using ANOVA F-test
selector_kbest = SelectKBest(score_func=f_classif, k=5)
X_kbest = selector_kbest.fit_transform(X_train, y_train)
print("# SelectKBest:", np.array(feature_names)[selector_kbest.get_support()])

# SelectPercentile using Chi2
selector_percentile = SelectPercentile(score_func=chi2, percentile=50)
X_percentile = selector_percentile.fit_transform(X_train, y_train)
print("# SelectPercentile (chi2):", np.array(feature_names)[selector_percentile.get_support()])

# GenericUnivariateSelect with mutual information
selector_generic = GenericUnivariateSelect(score_func=mutual_info_classif, mode='k_best', param=5)
X_generic = selector_generic.fit_transform(X_train, y_train)
print("# GenericUnivariateSelect:", np.array(feature_names)[selector_generic.get_support()])

# VarianceThreshold to remove low-variance features
selector_variance = VarianceThreshold(threshold=0.1)
X_variance = selector_variance.fit_transform(X_train)
print("# VarianceThreshold:", np.array(feature_names)[selector_variance.get_support()])

# ----------------------------
# 2. Wrapper Methods
# ----------------------------

# RFE with Logistic Regression
model_rfe = LogisticRegression(solver='liblinear')
selector_rfe = RFE(model_rfe, n_features_to_select=5)
X_rfe = selector_rfe.fit_transform(X_train, y_train)
print("# RFE:", np.array(feature_names)[selector_rfe.get_support()])

# RFECV with cross-validation
model_rfecv = LogisticRegression(solver='liblinear')
selector_rfecv = RFECV(model_rfecv, cv=5)
X_rfecv = selector_rfecv.fit_transform(X_train, y_train)
print("# RFECV:", np.array(feature_names)[selector_rfecv.get_support()])

# ----------------------------
# 3. Embedded Methods
# ----------------------------

# SelectFromModel with Lasso (L1 regularization)
model_lasso = Lasso(alpha=0.01)
selector_lasso = SelectFromModel(model_lasso)
selector_lasso.fit(X_train, y_train)
print("# SelectFromModel (Lasso):", np.array(feature_names)[selector_lasso.get_support()])

# SelectFromModel with tree-based feature importances
model_tree = RandomForestClassifier()
selector_tree = SelectFromModel(model_tree)
selector_tree.fit(X_train, y_train)
print("# SelectFromModel (RandomForest):", np.array(feature_names)[selector_tree.get_support()])

# SelectFromModel with LinearSVC (L1 penalty)
model_svc = LinearSVC(penalty='l1', dual=False, max_iter=2000)
selector_svc = SelectFromModel(model_svc)
selector_svc.fit(X_train, y_train)
print("# SelectFromModel (LinearSVC):", np.array(feature_names)[selector_svc.get_support()])
