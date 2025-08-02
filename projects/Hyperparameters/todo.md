1.
The dataset and some of the libraries you’ll use have been loaded on the setup cell. Run the setup cell to get started!

2.
Create the predictor and target variables and label them X and y respectively.

3.
Examine the dataset by printing the

total number of features
total number of samples
samples belonging to class “1”
4.
Split the training data into train and test data with a random_state of 19 (if you want to match the solution code - you’re welcome to use your preferred random_state too! :) . Label the training data X_train and y_train and the test data, X_test and y_test.

Grid Search with Decision Tree Classifier
5.
A decision tree classifier works well for a binary balanced class classification problem. Initialize a decision tree classifier named tree.

6.
The DecisionTreeClassifier() implementation in scikit-learn has many parameters.

Create a dictionary parameters to set up grid search to explore three values each for the following 2 hyperparameters:

'max_depth': The maximum tree depth; explore the values 3,5 and 7 for this.
'min_samples_split': The minimum number of samples to split at each node; explore the values 2,3 and 4 for this.
7.
Create a grid search classifier grid with tree and parameters as inputs. Fit the grid search classifier to the training data.

8.
Use the .best_estimator_ attribute to see what hyperparameters grid chose. Print the result. Print the best score and the score on the test data to examine the performance of the best estimator.

9.
Use .cv_results_['mean_test_score'] to get the score for for each hyperparameter combination. Get the corresponding hyperparameters with .cv_results_['params'].

Convert the two arrays to DataFrames, concatenate them using pd.concat and print it to view the score for each hyperparameter combination.

Random Search with Logistic Regression
10.
Define a logistic regression model, lr, with solver set to 'liblinear' and max_iter = 1000.

11.
To perform random search we need to specify the parameters and the distributions to draw from. Define a dictionary distributions with the keys

'penalty': corresponding to the type of regularization to apply. Choose a discrete distribution with ‘l1’ and ‘l2’
'C': corresponding to the regularization strength. Choose a uniform distribution here between 0 and 100.
12.
Create a model named clf to perform random search with the logistic regression model you’ve defined, over the distribution space specified by distributions and for eight random draws. Fit the model to the training data.

13.
Print the best estimator and score from the random search you’ve performed. Print a table summarizing the results using .cv_results_ similar to the way you did for grid search!

14.
Congratulations, you’ve completed the hyperparameter tuning project! Some points to ponder:

Examine your results to see which model performs best over all. Are there other models and hyperparameters you can think of to experiment with this dataset? (K-nearest neighbors or Support Vector Machines or gradient boosted trees might be other models to consider!)
Would you make different choices with the models you’ve used? Fire up your own Jupyter notebook to explore more models and alternate parameter grids/distributions! :)