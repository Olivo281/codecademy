import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris # Using Iris for LDA as it's good for classification

# --- 1. Load a dataset suitable for classification ---
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print(f"Original Iris data shape: {X.shape} (4 features, {len(target_names)} classes)")
print(f"Target classes: {target_names}\n")

# --- 2. Split data into training and testing sets ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
# #ImportantNote: stratify=y ensures that the proportion of classes is the same in train and test sets.

# --- 3. Standardize the data ---
# Scaling is crucial for LDA, especially if features have different scales.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- 4. Apply Linear Discriminant Analysis (LDA) ---
# For classification problems, the number of components in LDA is at most
# (number of classes - 1). For Iris (3 classes), max components = 2.
n_components_lda = min(X_train.shape[1], len(np.unique(y)) - 1)
lda = LinearDiscriminantAnalysis(n_components=n_components_lda)

# Fit LDA on the training data and transform both train and test sets
X_train_lda = lda.fit_transform(X_train_scaled, y_train)
# #ExplanationLDA: LDA learns the best projection based on the class labels in y_train.
# #ExplanationLDA: It's a supervised method, unlike PCA/SVD which are unsupervised.

X_test_lda = lda.transform(X_test_scaled)
# #ExplanationLDA: We only transform the test data using the projection learned from the training data.

print(f"Original training data shape: {X_train_scaled.shape}")
print(f"LDA transformed training data shape: {X_train_lda.shape} (reduced to {n_components_lda} components)\n")

# --- 5. Train a Classifier on the LDA-transformed data ---
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train_lda, y_train)

# --- 6. Evaluate the Classifier ---
y_pred = classifier.predict(X_test_lda)

print("--- Classification Results with LDA ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=target_names))

# --- Visualize the LDA-reduced data ---
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_train_lda[:, 0], y=X_train_lda[:, 1], hue=y_train, palette='viridis', legend='full')
plt.title(f'Iris Dataset after LDA (Reduced to {n_components_lda} Components)')
plt.xlabel('LDA Component 1')
plt.ylabel('LDA Component 2')
plt.grid(True)
plt.show()

# #HashtagExplanationForLDA: Notice how LDA tries to maximize the separation between the classes.
# #HashtagExplanationForLDA: The components it finds are directions that best discriminate between the groups.

# You can also look at the explained variance ratio for LDA
# (though it's interpreted slightly differently than PCA/SVD variance)
print("\nLDA Explained Variance Ratio:")
print(lda.explained_variance_ratio_)
# #HashtagExplanationForLDA: For LDA, this represents the proportion of the between-class variance
# #HashtagExplanationForLDA: captured by each discriminant function.
print(f"Total LDA explained variance by {n_components_lda} components: {lda.explained_variance_ratio_.sum():.4f}")