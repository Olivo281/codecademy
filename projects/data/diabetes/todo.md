
First, familiarize yourself with the dataset here.

Look at each of the nine columns in the documentation.

What do you expect each data type to be?

2.
Next, let’s load in the diabetes data to start exploring.

Load the data in a variable called diabetes_data and print the first few rows.

Note: The data is stored in a file called diabetes.csv.

3.
How many columns (features) does the data contain?

4.
How many rows (observations) does the data contain?

Further Inspection
5.
Let’s inspect diabetes_data further.

Do any of the columns in the data contain null (missing) values?

6.
If you answered no to the question above, not so fast!

While it’s technically true that none of the columns contain null values, that doesn’t necessarily mean that the data isn’t missing any values.

When exploring data, you should always question your assumptions and try to dig deeper.

To investigate further, calculate summary statistics on diabetes_data using the .describe() method.

7.
Looking at the summary statistics, do you notice anything odd about the following columns?

Glucose
BloodPressure
SkinThickness
Insulin
BMI
8.
Do you spot any other outliers in the data?

9.
Let’s see if we can get a more accurate view of the missing values in the data.

Use the following code to replace the instances of 0 with NaN in the five columns mentioned:

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

Copy to Clipboard

10.
Next, check for missing (null) values in all of the columns just like you did in Step 5.

Now how many missing values are there?

11.
Let’s take a closer look at these rows to get a better idea of why some data might be missing.

Print out all of the rows that contain missing (null) values.

12.
Go through the rows with missing data. Do you notice any patterns or overlaps between the missing data?

13.
Next, take a closer look at the data types of each column in diabetes_data.

Does the result match what you would expect?

14.
To figure out why the Outcome column is of type object (string) instead of type int64, print out the unique values in the Outcome column.

15.
How might you resolve this issue?

Next Steps
16.
Congratulations! In this project, you saw how EDA can help with the initial data inspection and cleaning process. This is an important step as it helps to keep your datasets clean and reliable.

Here are some ways you might extend this project if you’d like:

Use .value_counts() to more fully explore the values in each column.
Investigate other outliers in the data that may be easily overlooked.
Instead of changing the 0 values in the five columns to NaN, try replacing the values with the median or mean of each column.