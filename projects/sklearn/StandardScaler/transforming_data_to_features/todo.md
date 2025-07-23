
Let’s start with some basic exploring by performing the following:

First, import your dataset. It is stored under a file named reviews.csv. Save it to a variable called reviews.

2.
Next, we want to look at the column names of our dataset along with their data types. Do the following two steps:

Print the column names of your dataset.
Check your features’ data types by printing .info().
Data Transformations
3.
Transform the recommended feature. Start by printing the feature’s .value_counts().

4.
Since this is a True/False feature, we want to transform it to 1 for True and 0 for False.

To do this, create a dictionary called binary_dict where:

The keys are what is currently in the recommended feature.
The values are what we want in the new column (0s and 1s).
Click the hint if you get stuck.

5.
Using binary_dict, transform the recommended column so that it will now be binary. Print the results using .value_counts() to confirm the transformation.

6.
Let’s run through a similar process to transform the rating feature. This is ordinal data so our transformation should make that more clear. Again, start by printing the .value_counts().

To check your output, click the hint.

7.
We want to make the following changes to the values:

‘Loved it’ → 5
‘Liked it’ → 4
‘Was okay’ → 3
‘Not great’ → 2
‘Hated it’ → 1
Create a dictionary called rating_dict where the keys are what is currently in the feature and the values are what we want in the new column. You can use the hierarchy listed above to make your dictionary.

8.
Using rating_dict, transform the rating column so it contains numerical values. Print the results using .value_counts() to confirm the transformation.

9.
Let’s now transform the department_name feature. This process will be slightly different, but start by printing the .value_counts() of the feature.

Use Panda’s get_dummies to one-hot encode our feature.
Attach the results back to our original data frame.
Print the column names to see!
10.
Use panda’s get_dummies() method to one-hot encode our feature. Assign this to a variable called one_hot.

11.
Join the results from one_hot back to our original data frame. Then print out the column names. What has been added?

12.
Let’s make one more feature transformation!

Transform the review_date feature.

This feature is listed as an object type, but we want this to be transformed into a date-time feature.

Transform review_date into a date-time feature.
Print the feature type to confirm the transformation.
Click the hint if you get stuck.

Scaling the Data
13.
The final step we will take in our transformation project is scaling our data. We notice that we have a wide range of numbers thus far, so it is best to put everything on the same scale.

Let’s get our data frame to only have the numerical features we created. If you get stuck, click the hint.

14.
Reset the index to be our clothing_id feature.

15.
We are ready to scale our data! Perform a .fit_transform() on our data set, and print the results to see how the features have changed.

16.
Congratulations!

You have successfully completed this transformation project. Transformations are an incredibly valuable skill to have. Great job!

Code Review