Machine Learning Workflow
image

A machine learning workflow has the following steps. Depending on the dataset, the question we’re trying to answer and the tech stack we’re working with, one or more of these steps can be omitted or combined with another. The steps are:

ETL (Extract, Transform and Load) data
Data Cleaning
Train-Test-Validation Split
EDA (Exploratory Data Analysis)
Feature Engineering (normalization, removing autocorrelations, discretization, etc.)
Model Selection and Implementation
Model Evaluation
Hyperparameter Tuning
Model Validation
Build ML pipeline!
We’re now going to go through each of these steps in detail.

1. Extract, Transform and Load (ETL) data
This process can look different depending on the data sources and the tech-stack you maybe working with at a specific company. It is often the case that data is stored in a SQL database with a cloud service provider like AWS, Digital Ocean, etc. Depending on the volume of data, an engineer would use a tool like PySpark to extract this data, transform it and load it into a local database. Some times this falls within the purview of a Machine Learning Engineer (MLE) but depending on the technical sophistication of the stack, there might be Data Engineer or a Pipeline Engineer performing this task instead.

2. Data Cleaning and Aggregation
This step is often combined with the previous one. This can involve a range of tasks depending on the form and type of data as well as the problem that the machine learning pipeline is being designed to solve. Some examples include: dealing with null or missing entries, conforming timestamps to a standard, carrying out aggregations like grouping events based on timestamps by the hour or day, grouping IP’s by location, etc. Since Spark is best suited to perform such tasks on big data, this task might very well be the “Transform” part of the aforementioned ETL step. Alternately, raw data might get handed over to a MLE who then does the same after the ETL step.

3. Train-Test-Validation Split
The next step before “editing” the data in any manner, is to perform the train-test-validation split. You are likely very familiar with the idea of training and test data &mash; scikit-learn‘s model_selection module has a train_test_split function that’s used to to this. If you have ever implemented a machine learning model using scikit-learn, you’ve likely written the following piece of code:

from sklearn.model_selection import train_test_split
# For feature matrix X and target variable y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

In the example above, we see that the test data makes up a third of the original dataset. The random_state argument is set to ensure reproducibility here — i.e., if we reused 42, it would split a certain dataset in the exact same manner. The training data is used to learn a model’s parameters and the test data is used to test its performance. For models in production, there’s a third portion of the dataset that’s set aside known as a holdout or validation dataset used to tune hyperparameters and/or to perform model validation later on. If you would like to revisit the train-test-validation split, checkout this article on the same.

image

The reason we don’t want to perform data manipulations before splitting the dataset into training, test and validation datasets is that we don’t want data points from one of these to influence the other. Suppose we needed a machine learning model to predict housing prices and wanted to standardize a feature like the size of an apartment, the average of this value would look different between the entire dataset and each of the individual datasets. Scaling the entire column to the average value misses the unique information contained within the subpopulations and will make the model evaluation and validation process less objective.

4. Exploratory Data Analysis
Exploratory Data Analysis or EDA in the context of a machine learning workflow, is the step of inspecting, analyzing and altering your data to get it ready for machine learning modeling. Often this is the step where decisions on how to deal with outliers, transform are made. Our EDA in Python course covers this topic exhaustively but specifically, the articles on performing EDA before supervised (classification or regression) or unsupervised learning models are worth checking out if you’d like a refresher.

5. Feature Engineering
Feature engineer refers to an umbrella of methods to prep, select and reduce features in a machine learning problem. This can involve methods that overlap with EDA such as normalization, removing autocorrelations, discretization, etc. Feature engineering can also involve using machine learning algorithms like PCA to reduce dimensionality or methods that are implemented during the model fitting step like regularization. If you’d like to brush up on feature engineering methods, the Feature Engineering Skill Path is for you!

6. Model Selection and Implementation
Now we’re ready to test out different machine learning models. The choice of the model depends on the attributes of the data one’s working with as well as the type of question we’re trying to answer. scikit-learn has a nifty cheatsheet to choose the right estimator.

7. Model Evaluation
We’re now getting into the iterative part of the workflow. Whatever model is built, it must be evaluated on the test data. For classification problems, metrics like accuracy, precision, recall, F1 score and AUROC scores indicate how performant the model is and for regression problems, scores like RMSE and R-squared are some commonly used metrics. If you’d like to review these ideas, check out this lesson on Evaluation metrics. Machine learning engineers iterate over different types of models to figure out the most optimal model for the problem at hand.

8. Hyperparameter Tuning
Once a model has been decided upon, it can be tuned for better performance. Hyperparameter tuning is essential in making sure that the model does not overfit or underfit the data. If you would like a refresher on what hyperparameters are and methods of tuning hyperparameters, the hyperparameter tuning module might be just for you!

This is key to how well the model is fitting known data and how well it’s able to generalize to new data as well. Hence hyperparameter tuning might be done on the validation or holdout dataset.

9. Model Validation
Model validation is the process of making sure that the model is still performant on data that it hasn’t seen at all — neither in the training phase nor in the test phase. This can be done either during the hyperparameter tuning step or after. Typically the same metrics used during the model evaluation phase needs to be used here as well so as to make a reasonable comparison with the former.

image

10. Build ML pipeline!
When a machine learning workflow is part of a production cycle, it is often the case that a model is tuned and updated based on incoming information. In other words the model that worked well on last month’s data might not be applicable for this month. It is the job of a Machine Learning Engineer or a Pipeline Engineer to make sure that the model deployed into production is thus flexible and alterable without affecting the rest of the codebase. ML pipelines allow one to do the same!

A ML pipeline is a modular sequence of objects that codifies and automates a ML workflow to make it efficient, reproducible and generalizable.

Summary
We’ve gone through each of the steps within a machine learning workflow in detail. We’re now ready to build ML workflows and turn them into pipelines!