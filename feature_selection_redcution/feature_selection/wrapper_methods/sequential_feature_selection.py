import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.datasets import load_breast_cancer # A slightly more complex dataset

# --- 1. Load a sample dataset ---
# We'll use the Breast Cancer Wisconsin (Diagnostic) dataset for a binary classification problem.
# It has 30 features, which is good for demonstrating feature selection.
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print("Original Features:")
print(X.columns.tolist())
print(f"Number of original features: {X.shape[1]}\n")

# --- 2. Split data into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- 3. Choose a machine learning model ---
# A RandomForestClassifier is a good choice for demonstrating feature selection
# as it's robust and often benefits from reduced dimensionality.
estimator = RandomForestClassifier(n_estimators=100, random_state=42)

# --- SFS Example: Forward Feature Selection (forward=True, floating=False) ---
print("--- SFS Example: Pure Forward Feature Selection ---")
# This is the standard forward selection algorithm.
# It starts with an empty set of features and adds the one that gives the best performance
# until the stopping criterion (k_features) is met or no further improvement is possible.

sfs_forward = SFS(estimator,
                  k_features='best',      # Selects the number of features that yield the best performance
                  forward=True,           # #KeyParameter: Set to True for Forward Selection
                  floating=False,         # #KeyParameter: Set to False for pure (non-floating) forward selection
                                          # #HashtagExplanationForFloating: When floating=False, once a feature is added,
                                          # #HashtagExplanationForFloating: it's not revisited for removal in subsequent steps.
                                          # #HashtagExplanationForFloating: This makes the algorithm faster but potentially less optimal (greedy).
                  scoring='accuracy',     # Metric to optimize (e.g., 'accuracy', 'f1', 'roc_auc')
                  cv=4,                   # Use 4-fold cross-validation to evaluate feature subsets
                  n_jobs=-1,              # Use all available CPU cores for parallel processing
                  verbose=2)              # Prints progress messages

sfs_forward = sfs_forward.fit(X_train, y_train)

print(f"\n# Pure Forward Selection Results:")
print(f"Selected features (indices): {sfs_forward.k_feature_idx_}")
print(f"Selected features (names): {sfs_forward.k_feature_names_}")
print(f"Best accuracy with selected features: {sfs_forward.k_score_:.4f}")

# --- Evaluate the model with selected features on the test set ---
X_train_selected_forward = sfs_forward.transform(X_train)
X_test_selected_forward = sfs_forward.transform(X_test)

estimator.fit(X_train_selected_forward, y_train)
y_pred_forward = estimator.predict(X_test_selected_forward)
test_accuracy_forward = accuracy_score(y_test, y_pred_forward)
print(f"Model accuracy on test set with pure forward selected features: {test_accuracy_forward:.4f}\n")


# --- SFS Example: Forward Floating Selection (forward=True, floating=True) ---
print("--- SFS Example: Forward Floating Selection (SFFS) ---")
# Sequential Forward Floating Selection (SFFS)
# This is a more exhaustive search. After adding a feature (like pure forward selection),
# it then checks if removing any of the *previously added* features would improve the score.
# This "floating" back-and-forth mechanism helps to escape local optima and potentially find a better feature subset.

sfs_sffs = SFS(estimator,
               k_features='best',
               forward=True,            # #KeyParameter: Still forward, but with floating ability
               floating=True,           # #KeyParameter: Set to True for Floating Selection (SFFS)
                                        # #HashtagExplanationForFloating: When floating=True, after adding a feature,
                                        # #HashtagExplanationForFloating: the algorithm will try to remove a feature
                                        # #HashtagExplanationForFloating: that was previously added if it improves the score.
                                        # #HashtagExplanationForFloating: This is less greedy and can find better subsets, but is more computationally intensive.
               scoring='accuracy',
               cv=4,
               n_jobs=-1,
               verbose=2)

sfs_sffs = sfs_sffs.fit(X_train, y_train)

print(f"\n# Forward Floating Selection (SFFS) Results:")
print(f"Selected features (indices): {sfs_sffs.k_feature_idx_}")
print(f"Selected features (names): {sfs_sffs.k_feature_names_}")
print(f"Best accuracy with selected features: {sfs_sffs.k_score_:.4f}")

X_train_selected_sffs = sfs_sffs.transform(X_train)
X_test_selected_sffs = sfs_sffs.transform(X_test)

estimator.fit(X_train_selected_sffs, y_train)
y_pred_sffs = estimator.predict(X_test_selected_sffs)
test_accuracy_sffs = accuracy_score(y_test, y_pred_sffs)
print(f"Model accuracy on test set with SFFS selected features: {test_accuracy_sffs:.4f}\n")


# --- SFS Example: Backward Elimination (forward=False, floating=False) ---
print("--- SFS Example: Pure Backward Elimination ---")
# This algorithm starts with ALL features and iteratively removes the one
# that causes the least decrease (or best increase) in performance.

sfs_backward = SFS(estimator,
                   k_features=1,           # #KeyParameter: Often set to a specific number or 'best' for backward.
                                           # For backward, k_features=1 means it will remove until only 1 is left.
                   forward=False,          # #KeyParameter: Set to False for Backward Elimination
                   floating=False,         # Set to False for pure (non-floating) backward elimination
                   scoring='accuracy',
                   cv=4,
                   n_jobs=-1,
                   verbose=2)

# It's important to start backward elimination with all features.
sfs_backward = sfs_backward.fit(X_train, y_train)

print(f"\n# Pure Backward Elimination Results:")
print(f"Selected features (indices): {sfs_backward.k_feature_idx_}")
print(f"Selected features (names): {sfs_backward.k_feature_names_}")
print(f"Best accuracy with selected features: {sfs_backward.k_score_:.4f}")

X_train_selected_backward = sfs_backward.transform(X_train)
X_test_selected_backward = sfs_backward.transform(X_test)

estimator.fit(X_train_selected_backward, y_train)
y_pred_backward = estimator.predict(X_test_selected_backward)
test_accuracy_backward = accuracy_score(y_test, y_pred_backward)
print(f"Model accuracy on test set with pure backward selected features: {test_accuracy_backward:.4f}\n")


# --- Explanation of All Parameters for SFS ---
print("\n--- Explanation of All Parameters for mlxtend.feature_selection.SequentialFeatureSelector ---")
print("\n**`estimator`**: (Required) A supervised learning estimator (e.g., classifier or regressor) that implements `fit` and `predict` (or `predict_proba` for 'roc_auc' scoring) methods. This is the model whose performance is used to evaluate feature subsets.")

print("\n**`k_features`**: (Required) The number of features to select.")
print("    - `int`: Selects exactly this many features.")
print("    - `tuple`: (min_features, max_features) - Selects the best subset within this range.")
print("    - `'best'`: Selects the number of features that results in the highest score.")
print("    - `'parsimonious'`: Selects the smallest subset of features that is within one standard error of the best score.")

print("\n**`forward`**: (`True` or `False`, default=`True`)")
print("    - `True`: Performs forward feature selection (adds features one by one).")
print("    - `False`: Performs backward feature elimination (removes features one by one).")

print("\n**`floating`**: (`True` or `False`, default=`False`)")
print("    - `True`: Enables 'floating' behavior (e.g., Sequential Forward Floating Selection (SFFS) or Sequential Backward Floating Selection (SBFS)).")
print("              After an addition/removal step, it performs conditional removal/addition of previously chosen/discarded features if it improves the score.")
print("              #HashtagExplanationForFloating: This makes the search more thorough and can find better global optima, but is more computationally expensive.")
print("    - `False`: Disables 'floating' behavior, resulting in pure sequential selection (greedy approach).")

print("\n**`scoring`**: (str, callable, or None, default=`None`)")
print("    - Metric to evaluate feature subsets. Examples: 'accuracy', 'f1', 'roc_auc' (for classification), 'neg_mean_squared_error', 'r2' (for regression).")
print("    - Can also be a custom scoring function compatible with scikit-learn's `make_scorer`.")
print("    - If `None`, uses the estimator's default scorer (e.g., `estimator.score(X, y)`).")

print("\n**`cv`**: (int, cross-validation generator, or iterable, default=`5`)")
print("    - Determines the cross-validation splitting strategy. E.g., `cv=5` for 5-fold cross-validation.")
print("    - Used to get a more robust estimate of performance for each feature subset.")

print("\n**`n_jobs`**: (int, default=`1`)")
print("    - Number of CPU cores to use for parallel computation during cross-validation.")
print("    - `-1` means use all available cores.")

print("\n**`verbose`**: (int, default=`0`)")
print("    - Controls the verbosity of the output.")
print("    - `0`: No output.")
print("    - `1`: Prints a simple progress bar.")
print("    - `2`: Prints detailed messages about each step and feature added/removed.")

print("\n**`fixed_features`**: (tuple, default=`None`)")
print("    - A tuple of feature indices (0-based) that should always be included in the feature subset. These features are not subject to selection or elimination.")

print("\n**`pre_dispatch`**: (int or str, default=`'n_jobs'`)")
print("    - Number of jobs to be dispatched to the parallel backend. Can be useful for fine-tuning performance with `n_jobs > 1`.")

print("\n**`custom_feature_names`**: (iterable, default=`None`)")
print("    - Optional list of strings that represent the names of the features, to be used instead of the column names of `X`.")