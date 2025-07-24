from sklearn.datasets import load_iris
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import randint

# Load data and split
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

# Define model
rf = RandomForestClassifier(random_state=42)

# Define hyperparameter distribution (random values sampled)
param_dist = {
    'n_estimators': randint(10, 200),
    'max_depth': randint(1, 20)
}

# Setup RandomizedSearchCV (try 10 random combinations)
random_search = RandomizedSearchCV(rf, param_dist, n_iter=10, cv=3, scoring='accuracy', random_state=42)
random_search.fit(X_train, y_train)

# Outputs
print("Best parameters:", random_search.best_params_)
print("Best cross-validation score:", random_search.best_score_)
print("Best estimator:", random_search.best_estimator_)

# Evaluate on test set
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Test set accuracy:", accuracy_score(y_test, y_pred))
