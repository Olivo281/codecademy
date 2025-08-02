import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
digits = datasets.load_digits()
# print(digits)
# print(digits.DESCR)
# print(digits.data)
# print(digits.target)

# plt.gray() 
# plt.matshow(digits.images[100])
# plt.show()
# print(digits.target[100])

model = KMeans(n_clusters = 10)
model.fit(digits.data)
fig = plt.figure(figsize=(8,3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')
for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

new_samples = np.array([
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.08,1.45,0.23,0.00,0.00,0.00,0.00,0.38,6.79,7.62,3.43,0.00,0.00,0.00,0.00,0.23,5.34,7.62,3.66,0.00,0.00,0.00,0.00,0.00,4.73,7.62,1.68,0.00,0.00,0.00,0.00,1.37,7.62,6.25,3.05,3.05,0.46,0.00,0.00,0.61,6.41,7.55,7.62,7.55,1.83,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.30,4.58,4.80,1.60,0.00,0.00,0.00,1.45,7.40,7.62,7.32,7.47,2.13,0.00,0.00,4.50,7.47,1.45,0.46,6.56,6.48,0.00,0.00,5.34,6.86,0.84,0.00,3.89,7.63,0.00,0.00,2.29,7.55,7.55,6.86,7.24,7.02,0.00,0.00,0.00,1.45,3.58,3.81,3.81,1.91,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.92,1.52,1.52,1.52,0.38,0.00,0.00,1.07,7.47,7.62,7.62,7.62,4.04,0.00,0.00,0.23,2.97,2.44,7.17,7.17,1.53,0.00,0.00,0.00,0.00,4.73,7.62,3.13,1.52,1.45,0.00,0.00,0.00,7.47,7.62,7.62,7.62,7.62,0.00,0.00,0.00,1.14,1.52,1.52,1.52,1.45,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00],
[0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.60,2.06,2.67,5.34,1.75,0.00,0.00,0.00,6.94,7.62,7.62,7.62,2.90,0.00,0.00,0.00,1.98,7.62,6.10,7.55,6.33,0.38,0.00,0.00,4.04,7.40,0.46,2.29,7.62,2.90,0.00,0.00,4.57,7.17,0.30,1.07,7.62,2.90,0.00,0.00,2.13,7.62,6.71,5.87,7.62,1.98,0.00,0.00,0.00,1.98,5.18,5.34,3.66,0.08,0.00,0.00]
])
new_labels = model.predict(new_samples)
for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, end='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')
