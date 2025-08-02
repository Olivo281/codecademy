from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()
# print(breast_cancer_data.data[0])
# print(breast_cancer_data.feature_names)
# print(breast_cancer_data.target)
# print(breast_cancer_data.target_names)

training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data,breast_cancer_data.target, test_size = .2, random_state = 100)

# print(len(training_data))
# print(len(training_labels))
scores_ = []
for i in range(1,101):
  classifier = KNeighborsClassifier(n_neighbors = i)
  classifier.fit(training_data, training_labels)
  scores_.append([classifier.score(validation_data, validation_labels),i])
y = [score[0] for score in scores_]
x = [score[1] for score in scores_]
plt.plot(x,y)
plt.xlabel('k')
plt.ylabel('score')
plt.title('Best n for KNeighbors')
plt.show()
scores_sorted = sorted(scores_)
print(scores_sorted[-5:])

