from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors = 5)

classifier.fit(movie_dataset,labels)
guess = classifier.predict([[.45, .2, .5], [.25, .8, .9], [.1, .1, .9]])
print(guess)

# with weighted regression
from movies import movie_dataset, movie_ratings
from sklearn.neighbors import KNeighborsRegressor

regressor = KNeighborsRegressor(n_neighbors = 5, weights = "distance")
regressor.fit(movie_dataset,movie_ratings)
print(regressor.predict([[0.016, 0.300, 1.022], [0.0004092981, 0.283, 1.0112], [0.00687649, 0.235, 1.0112]]))

