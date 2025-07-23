from sklearn.metrics import (
    # Regression
    mean_squared_error, mean_absolute_error, r2_score, median_absolute_error, mean_squared_log_error,

    # Classification
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve, log_loss, matthews_corrcoef, hamming_loss, hinge_loss, jaccard_score,
    zero_one_loss, balanced_accuracy_score,

    # Multilabel / multiclass
    multilabel_confusion_matrix, average_precision_score, top_k_accuracy_score,

    # Clustering
    adjusted_rand_score, normalized_mutual_info_score, silhouette_score, calinski_harabasz_score,
    davies_bouldin_score, adjusted_mutual_info_score,

    # Ranking
    ndcg_score, dcg_score
)

import numpy as np
from sklearn.datasets import make_classification, make_regression, make_blobs
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression

# ------------------- Regression Metrics ------------------- #
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=10)
X_train, X_test, y_train, y_test = train_test_split(X_reg, y_reg, random_state=42)
reg = LinearRegression().fit(X_train, X_train * 3 + 7 + np.random.randn(*X_train.shape))  # simulate poor fit
y_pred = reg.predict(X_test)

print("Regression Metrics:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))
print("Median Absolute Error:", median_absolute_error(y_test, y_pred))
print("Mean Squared Log Error:", mean_squared_log_error(np.abs(y_test)+1, np.abs(y_pred)+1))  # log error needs positive

# ------------------- Classification Metrics ------------------- #
X_clf, y_clf = make_classification(n_samples=100, n_classes=2, n_informative=2, n_features=5, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, random_state=42)
clf = LogisticRegression().fit(X_train, y_train)
y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)[:, 1]

print("\nClassification Metrics:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_proba))
print("Log Loss:", log_loss(y_test, y_proba))
print("Matthews Corrcoef:", matthews_corrcoef(y_test, y_pred))
print("Hamming Loss:", hamming_loss(y_test, y_pred))
print("Jaccard Score:", jaccard_score(y_test, y_pred))
print("Zero-One Loss:", zero_one_loss(y_test, y_pred))
print("Balanced Accuracy:", balanced_accuracy_score(y_test, y_pred))

# ------------------- Clustering Metrics ------------------- #
X_cluster, y_true = make_blobs(n_samples=100, centers=3, random_state=42)
kmeans = KMeans(n_clusters=3, random_state=42).fit(X_cluster)
y_kmeans = kmeans.labels_

print("\nClustering Metrics:")
print("Adjusted Rand Index:", adjusted_rand_score(y_true, y_kmeans))
print("Adjusted Mutual Info:", adjusted_mutual_info_score(y_true, y_kmeans))
print("Normalized Mutual Info:", normalized_mutual_info_score(y_true, y_kmeans))
print("Silhouette Score:", silhouette_score(X_cluster, y_kmeans))
print("Calinski-Harabasz Score:", calinski_harabasz_score(X_cluster, y_kmeans))
print("Davies-Bouldin Score:", davies_bouldin_score(X_cluster, y_kmeans))

# ------------------- Ranking Metrics ------------------- #
y_true_ranking = np.asarray([[0, 1, 1]])
y_score_ranking = np.asarray([[0.1, 0.4, 0.35]])

print("\nRanking Metrics:")
print("NDCG Score:", ndcg_score(y_true_ranking, y_score_ranking))
print("DCG Score:", dcg_score(y_true_ranking, y_score_ranking))

# ------------------- Multilabel & Top-K ------------------- #
y_true_ml = np.array([[1, 0, 1], [0, 1, 0]])
y_pred_ml = np.array([[1, 0, 0], [0, 1, 1]])
y_score_ml = np.array([[0.9, 0.1, 0.3], [0.2, 0.8, 0.6]])

print("\nMultilabel Metrics:")
print("Multilabel Confusion Matrix:\n", multilabel_confusion_matrix(y_true_ml, y_pred_ml))
print("Average Precision Score:", average_precision_score(y_true_ml, y_score_ml))
print("Top-K Accuracy Score:", top_k_accuracy_score(y_true_ml, y_score_ml, k=2))
