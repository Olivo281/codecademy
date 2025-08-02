import pandas as pd
import numpy as np
import codecademylib3

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

path_to_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

col_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
    'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
    'hours-per-week', 'native-country', 'income'
]

df = pd.read_csv(path_to_data, header=None, names=col_names)

# 3. Clean categorical variables
for c in df.select_dtypes(include=['object']).columns:
    df[c] = df[c].str.strip()

# 4. Percentage of samples by income group
less_than = df['income'] == '>50K'
more_than = df['income'] == '<=50K'
total = len(df['income'])
less_perc = less_than.sum() / total * 100
more_perc = more_than.sum() / total * 100
print(f"Percentage >50K: {less_perc:.2f}%")
print(f"Percentage <=50K: {more_perc:.2f}%")

# 5. Data types
print("\nData Types:")
for col in df.columns:
    print(f"{col}: {df[col].dtype}")

# 6. Prepare features
raw_feature_cols = ['age', 'education-num', 'workclass', 'hours-per-week', 'sex', 'race']
X = pd.get_dummies(df[raw_feature_cols], drop_first=True)
print("\nFeatures preview:")
print(X.head())

# 7. Convert target variable to binary
y = df['income'].apply(lambda x: 1 if x == '>50K' else 0)

# 8. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 9. Decision stump
decision_stump = DecisionTreeClassifier(max_depth=1, random_state=42)

# 10. AdaBoost Classifier
ada_classifier = AdaBoostClassifier(base_estimator=decision_stump, random_state=42)

# 11. Gradient Boosting Classifier
grad_classifier = GradientBoostingClassifier(random_state=42)

# 12. Fit models
ada_classifier.fit(X_train, y_train)
grad_classifier.fit(X_train, y_train)

# 13. Predictions
y_pred_ada = ada_classifier.predict(X_test)
y_pred_grad = grad_classifier.predict(X_test)

# 14. Evaluation
print("\nModel Performance:")
print("AdaBoost - Accuracy:", accuracy_score(y_test, y_pred_ada))
print("AdaBoost - F1 Score:", f1_score(y_test, y_pred_ada))
print("Gradient Boosting - Accuracy:", accuracy_score(y_test, y_pred_grad))
print("Gradient Boosting - F1 Score:", f1_score(y_test, y_pred_grad))

# 15. Hyperparameter Tuning (AdaBoost)
n_estimators_list = [10, 30, 50, 70, 90]
param_grid = {'n_estimators': n_estimators_list}

grid_search = GridSearchCV(
    AdaBoostClassifier(base_estimator=decision_stump, random_state=42),
    param_grid,
    scoring='f1',
    cv=5
)

grid_search.fit(X_train, y_train)
ada_scores_list = grid_search.cv_results_['mean_test_score']

# 16. Plot results
plt.figure(figsize=(8, 5))
plt.plot(n_estimators_list, ada_scores_list, marker='o')
plt.xlabel('Number of Estimators')
plt.ylabel('Mean F1 Score (CV)')
plt.title('AdaBoost F1 Score vs. n_estimators')
plt.grid(True)
plt.show()

# 17. Best parameters
print("\nBest AdaBoost Params from Grid Search:")
print("Best n_estimators:", grid_search.best_params_['n_estimators'])
print("Best F1 Score:", grid_search.best_score_)