# Step 1: Setup
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from scipy.stats import uniform
import numpy as np

# Load the dataset
raisins = pd.read_csv('Raisin_Dataset.csv')
print(raisins.head())

# Step 2: Create X (features) and y (target)
X = raisins.drop(columns=['Class'])
y = raisins['Class']

# Step 3: Explore dataset
print("Total number of features:", X.shape[1])
print("Total number of samples:", X.shape[0])
print("Samples belonging to class 'Kecimen':", sum(y == 'Kecimen'))

# Step 4: Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=19
)

# Step 5: Initialize Decision Tree
tree = DecisionTreeClassifier()

# Step 6: Grid Search Parameters
parameters = {
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 3, 4]
}

# Step 7: Perform Grid Search
grid = GridSearchCV(tree, parameters, cv=5)
grid.fit(X_train, y_train)

# Step 8: Print best estimator, scores
print("\n📌 Grid Search Results")
print("Best Estimator:", grid.best_estimator_)
print("Best Cross-validation Score:", grid.best_score_)
print("Test Score:", grid.score(X_test, y_test))

# Step 9: Show all combinations
grid_scores_df = pd.DataFrame(grid.cv_results_['params'])
grid_scores_df['mean_test_score'] = grid.cv_results_['mean_test_score']
print("\nGrid Search Hyperparameter Combinations and Scores:")
print(grid_scores_df)

# Step 10: Define Logistic Regression
lr = LogisticRegression(solver='liblinear', max_iter=1000)

# Step 11: Define Random Search Distributions
distributions = {
    'penalty': ['l1', 'l2'],
    'C': uniform(loc=0, scale=100)
}

# Step 12: Perform Random Search
clf = RandomizedSearchCV(lr, distributions, n_iter=8, random_state=19, cv=5)
clf.fit(X_train, y_train)

# Step 13: Print results
print("\n📌 Random Search Results")
print("Best Estimator:", clf.best_estimator_)
print("Best Cross-validation Score:", clf.best_score_)
print("Test Score:", clf.score(X_test, y_test))

random_scores_df = pd.DataFrame(clf.cv_results_['params'])
random_scores_df['mean_test_score'] = clf.cv_results_['mean_test_score']
print("\nRandom Search Hyperparameter Combinations and Scores:")
print(random_scores_df)
