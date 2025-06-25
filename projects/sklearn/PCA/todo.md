
Remove any nulls from the dataset.

2.
Extract the numerical columns onto a variable named data_matrix and the classes to a variable named classes

3.
Create a correlation matrix of the data matrix and show it as a heatmap.

4.
Find the eigenvectors and eigenvalues using the NumPy function np.linalg.eig. Here we also order the eigenvalues from greatest to smallest by ordering its indices first, and use these indices to also order the eigenvalues.

5.
Find the proportions of each eigenvalue to the total sum of the eigenvalues. These proportions represent the percentages of information that each eigenvalue’s associated eigenvector contains.

6.
Find the cumulative percentages of the ordered eigenvectors.

Performing PCA
7.
Recall that PCA uses the standardized matrix, which scales for the mean and standard deviation. Calculate the standardized data matrix.

8.
Using the sklearn module PCA, perform PCA by fitting and transforming the standardized data matrix.

9.
Using the properties of the PCA trained object, pca, calculate the eigenvalues from the singular values and extract the eigenvectors.

10.
Using the properties of the pca trained object, extract the variance ratios, which are equivalent to the eigenvalue proportions we calculated earlier.

11.
Perform PCA once again but with 2 principal axes. Make sure to fit and transform the standardized data matrix.

12.
Plot the principal components and have its class as its hue to see if clustering of any kind has occurred.

13.
Once again, we will perform PCA on 2 components, but we will also use the newly transformed PCA features as input to a support vector classifier! Fit the transformed features onto the classifier and generate a score.

14.
Now, fit the classifier with the first two features of the original standardized data matrix and generate a score.

Looking at the two SVG models, the first model with the PCA features and the second model with the original data features, which model has a higher accuracy score?