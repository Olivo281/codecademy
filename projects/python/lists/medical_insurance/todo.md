First, take a look at the two lists in script.py.

The list names stores the names of ten individuals, and insurance_costs stores their medical insurance costs.

Let’s add additional data to these lists:

Append a new individual, "Priscilla", to names.
Append her insurance cost, 8320.0, to insurance_costs.
2.
Currently, the names and insurance_costs lists are separate, but we want each insurance cost to be paired with a name.

Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function.

The list should have the following structure:

[(cost_0, name_0), (cost_1, name_1), (cost_2, name_2), ...]

Copy to Clipboard

3.
Print out medical_records in the terminal, and make sure the output is what you expected.

4.
Let’s explore our medical data.

We want to see how many medical records we’re dealing with. Create a variable called num_medical_records that stores the length of medical_records.

5.
Print num_medical_records with the following message:

There are {number of medical records} medical records. 

Copy to Clipboard

Selecting List Elements
6.
Select the first medical record in medical_records, and save it to a variable called first_medical_record.

7.
Print first_medical_record with the following message:

Here is the first medical record: {first medical record}

Copy to Clipboard

Sorting Lists
8.
Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.

Print the sorted medical_records with the following message:

Here are the medical records sorted by insurance cost: {sorted list}

Copy to Clipboard

Slicing Lists
9.
Let’s look at the three cheapest insurance costs in our medical records.

Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.

10.
Print cheapest_three with the following message:

Here are the three cheapest insurance costs in our medical records: {cheapest three}

Copy to Clipboard

11.
Let’s look at the three most expensive insurance costs in our medical records.

Slice the medical_records list, and store the three most expensive insurance costs in a list called priciest_three.

12.
Print priciest_three with the following message:

Here are the three most expensive insurance costs in our medical records: {priciest three}

Copy to Clipboard

Counting Elements in a List
13.
Some individuals in our medical records have the same name. For example, the name “Paul” shows up twice.

Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.

Print occurrences_paul with the following message:

There are {occurrences Paul} individuals with the name Paul in our medical records. 

Copy to Clipboard

Extra
14.
Great job! In this project, you worked with Python lists to store medical insurance cost data and then gained meaningful insight into that data.

You now have a better understanding of how to interact with data in lists – an important skill for a data scientist to have.

Our dataset in this project was pretty small – we only dealt with 11 medical records. However, as you progress in your data science journey, you will encounter larger and more complex datasets. You are now better prepared to work with data in lists moving forward.

If you’d like additional practice on lists, here are some ways you might extend this project:

Sort the medical records alphabetically by name. You’ll have to create a new list using zip() to do this.
Select the medical records starting at index 3 and ending at index 7 and save it in a variable called middle_five_records.
Happy coding!