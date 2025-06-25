
First, let’s take a look at the three lists in script.py:

names stores the names of seven individuals.
estimated_insurance_costs stores the estimated medical insurance costs for the individuals.
actual_insurance_costs stores the actual insurance costs paid by the individuals.
We want to calculate the average insurance cost each person paid. We’ll start by adding up all of the insurance costs.

Create a variable total_cost and initialize it to 0.

2.
Use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost.

3.
After the for loop, create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.

4.
Print average_cost with the following message:

Average Insurance Cost: <average_cost> dollars.

Copy to Clipboard

Using Range in Loops
5.
For each individual in names, we want to determine whether their insurance cost is above or below average.

Write a for loop with variable i that goes from 0 to len(names).

Note: If you run this loop it will return an error because there is currently no code inside of the loop. We’ll fix this in the next step.

6.
Inside of the for loop, do the following:

Create a variable name, which stores names[i].
Create a variable insurance_cost, which stores actual_insurance_costs[i].
Print out the insurance cost for each individual, with the following message:
The insurance cost for <name> is <insurance_cost> dollars.

Copy to Clipboard

7.
Click “Save” to see the result.

You should see the insurance costs for each of the seven individuals in names. The for loop iterated through the entire list and printed out the insurance cost for each individual.

Conditions inside a Loop
8.
Inside of the for loop, use if, elif, else statements after the print statement to check whether the insurance cost is above, below, or equal to the average. Print out messages for each case:

When insurance_cost is higher than the average, print out the following:
The insurance cost for <name> is above average.

Copy to Clipboard

When insurance_cost is lower than the average, print out the following:
The insurance cost for <name> is below average.

Copy to Clipboard

Otherwise, print out the following:
The insurance cost for <name> is equal to the average.

Copy to Clipboard

9.
Click “Save” to see the results.

You should see messages indicating the insurance cost for each of the seven individuals and where their insurance cost stands relative to the average.

Creating a List Comprehension
10.
If you look closely at actual_insurance_costs and estimated_insurance_costs, you will notice that each of the actual insurance costs are 10% higher than the estimated insurance costs.

Using a list comprehension, create a new list called updated_estimated_costs, which has each element in estimated_insurance_costs multiplied by 11/10.

11.
Print updated_estimated_costs.

You should see that the list now looks the same as actual_insurance_costs.

Extra
12.
Congratulations! In this project, you used Python loops to iterate through and analyze medical insurance cost data.

As a data scientist, you want to be able to easily and efficiently go through data and perform analysis on that data without having to write repetitive code. Loops are a great place to start.

If you’d like extra practice with Python loops, here are some suggestions to get you started:

Convert the first for loop in the code to a while loop.
Modify the second for loop so that it also calculates how far above or below the average the estimated insurance cost is.
Happy coding!