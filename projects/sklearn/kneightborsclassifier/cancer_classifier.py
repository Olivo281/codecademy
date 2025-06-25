# 1. Importing necessary libraries and loading the dataset
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load the breast cancer dataset
breast_cancer_data = load_breast_cancer()

# 2. Print the first data point and feature names
print("First data point:")
print(breast_cancer_data.data[0])

print("\nFeature names:")
print(breast_cancer_data.feature_names)

# 3. Print the target values and what they represent
print("\nTarget values:")
print(breast_cancer_data.target)

print("\nTarget names:")
print(breast_cancer_data.target_names)

# Was the first data point malignant or benign?
first_target = breast_cancer_data.target[0]
print(f"\nFirst data point is classified as: {breast_cancer_data.target_names[first_target]}")

# 4. Import train_test_split (already done above)

# 5 & 6. Split data into training and validation sets
training_data, validation_data, training_labels, validation_labels = train_test_split(
    breast_cancer_data.data, 
    breast_cancer_data.target, 
    test_size=0.2, 
    random_state=100
)

# 7. Confirm sizes match
print(f"\nTraining data size: {len(training_data)}")
print(f"Training labels size: {len(training_labels)}")

# 8 & 9. Train a KNN classifier (try different values of k from 1 to 100)
accuracies = []
k_list = list(range(1, 101))

for k in k_list:
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)
    accuracy = classifier.score(validation_data, validation_labels)
    accuracies.append(accuracy)

# 12–17. Plotting the results
plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()

# 18. Optional: Print top 5 k values with highest accuracy
top_k_scores = sorted(zip(accuracies, k_list), reverse=True)[:5]
print("\nTop 5 k values with highest validation accuracy:")
for score, k in top_k_scores:
    print(f"k = {k}: Accuracy = {score:.4f}")
