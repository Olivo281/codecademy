
We would like to keep a record of medical patients and their insurance costs.

First, create an empty dictionary called medical_costs.

2.
Let’s populate our medical_costs dictionary by adding the following key-value pairs:

Add "Marina" to medical_costs as a key with a value of 6607.0.
Add "Vinay" to medical_costs as a key with a value of 3225.0.
3.
Using one line of code, add the following three patients to the medical_costs dictionary:

"Connie", with an insurance cost of 8886.0
"Isaac", with an insurance cost of 16444.0
"Valentina", with an insurance cost of 6420.0
4.
Print medical_costs. Make sure the dictionary is what you expected.

5.
You notice that Vinay’s insurance cost was incorrectly inputted. Update the value associated with Vinay to 3325.0.

Print the updated dictionary.

6.
Let’s calculate the average medical cost of each patient. Create a variable called total_cost and set it equal to 0.

Next, iterate through the values in medical_costs and add each value to the total_cost variable.

7.
After the loop, create a variable called average_cost that stores the total_cost divided by the length of the medical_costs dictionary.

Print average_cost with the following message:

Average Insurance Cost: {average_cost}

Copy to Clipboard

List Comprehension to Dictionary
8.
You have been asked to create a second dictionary that maps patient names to their ages.

First, create two lists called names and ages with the following data:

names	ages
Marina	27
Vinay	24
Connie	43
Isaac	35
Valentina	52
9.
Next, create a variable called zipped_ages that is a zipped list of pairs between the names list and the ages list.

10.
Create a dictionary called names_to_ages by using a list comprehension that iterates through zipped_ages and turns each pair into a key : value item.

Print names_to_ages to see the result.

11.
Use .get() to get the value of Marina’s age and store it in a variable called marina_age. Use None as a default value if the key doesn’t exist.

Print marina_age with the following message:

Marina's age is {marina_age}

Copy to Clipboard

Using a Dictionary to create a medical database
12.
Let’s create a third dictionary to represent a database of medical records that contains information such as a patient’s name, age, sex, gender, BMI, number of children, smoker status, and insurance cost.

First, create an empty dictionary called medical_records.

13.
Next, add "Marina" to medical_records as a key with the value being a dictionary of medical data:

{"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

Copy to Clipboard

14.
Do the same for the following individuals:

Name	Age	Sex	BMI	Children	Smoker	Insurance Cost
Vinay	24	Male	26.9	0	Non-smoker	3225.0
Connie	43	Female	25.3	3	Non-smoker	8886.0
Isaac	35	Male	20.6	4	Smoker	16444.0
Valentina	52	Female	18.7	1	Non-smoker	6420.0
15.
Print medical_records to see the result.

16.
The medical_records dictionary acts like a database of medical records. Let’s access a specific piece of data in medical_records.

Print out Connie’s insurance cost with the following message:

Connie's insurance cost is X dollars.

Copy to Clipboard

17.
Vinay has moved to a new country and we no longer want to include him in our medical records.

Remove Vinay from medical_records.

18.
Let’s take a closer look at each patient’s medical record.

Use a for loop to iterate through the items of medical_records. For each key-value pair, print out a string that looks like the following:

{Name} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}

Copy to Clipboard

Extra
19.
Congratulations! In this project, you used Python dictionaries to store and update medical data for individuals.

If you’d like extra practice with dictionaries, here are some suggestions to go further with this project:

Create a function called update_medical_records() that takes in the name of an individual as well as their medical data, and then updates the medical_records dictionary accordingly.
Create a new dictionary of your choice – feel free to get creative!
Happy coding!