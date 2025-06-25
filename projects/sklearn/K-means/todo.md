Getting Started with the Digits Dataset:
1.
The sklearn library comes with a digits dataset for practice.

In script.py, we have already added three lines of code:

import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt

Copy to Clipboard

From sklearn library, import the datasets module.

Then, load in the digits data using .load_digits() and print digits.

2.
When first starting out with a dataset, it’s always a good idea to go through the data description and see what you can already learn.

Instead of printing the digits, print digits.DESCR.

What is the size of an image (in pixel)?
Where is this dataset from?
3.
Let’s see what the data looks like!

Print digits.data.

4.
Next, print out the target values in digits.target.

5.
To visualize the data images, we need to use Matplotlib. Let’s visualize the image at index 100:

plt.gray() 

plt.matshow(digits.images[100])

plt.show()

Copy to Clipboard

The image should look like:

4

Is it a 4? Let’s print out the target label at index 100 to find out!

print(digits.target[100])

Copy to Clipboard

Open the hint to see how you can visualize more than one image.

K-Means Clustering:
6.
Now we understand what we are working with. Let’s cluster the 1797 different digit images into groups.

Import KMeans from sklearn.cluster.

7.
What should be the k, the number of clusters, here?

Use the KMeans() method to build a model that finds k clusters.

8.
Use the .fit() method to fit the digits.data to the model.

Visualizing after K-Means:
9.
Let’s visualize all the centroids! Because data samples live in a 64-dimensional space, the centroids have values so they can be images!

First, add a figure of size 8x3 using .figure().

Then, add a title using .suptitle().

10.
Scikit-learn sometimes calls centroids “cluster centers”.

Write a for loop to displays each of the cluster_centers_ like so:

for i in range(10):

  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)

  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

Copy to Clipboard

The cluster centers should be a list with 64 values (0-16). Here, we are making each of the cluster centers into an 8x8 2D array.

11.
Outside of the for loop, use .show() to display the visualization.

Did it work?

These are the centroids of handwriting from thirty different people collected by Bogazici University (Istanbul, Turkey):

Index 0 looks like 0
Index 1 looks like 9
Index 2 looks like 2
Index 3 looks like 1
Index 4 looks like 6
Index 5 looks like 8
Index 6 looks like 4
Index 7 looks like 5
Index 8 looks like 7
Index 9 looks like 3
Notice how the centroids that look like 1 and 8 look very similar and 1 and 4 also look very similar.

12.
Optional:

If you want to see another example that visualizes the data clusters and their centers using K-means, check out the sklearn‘s own example.

K-means clustering example

You will get a different K-means clustering map each time you run a new K-means model.

Testing Your Model:
13.
Instead of feeding new arrays into the model, let’s do something cooler!

Inside the right panel, go to test.html.

14.
What year will robots take over the world?

Use your mouse to write a digit in each of the boxes and click Get Array.