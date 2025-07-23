
Let’s start with creating the count() function.

Inside the count() function, write a filter() function that will “filter” itr based on predicate. Save this value to a variable called count_filter.

2.
Inside of count(), use reduce() to process the iterator returned from filter() so the accumulator imcrements by one for each True evaluation from filter().

Remember this definition of reduce():

reduce(lambda x, y: x + y, some_collection, initial_value)

Copy to Clipboard

Save your reduce() function to a variable called count_reduce. Make sure to return count_reduce at the end of your function.

Click the hint or check solution.py if you feel stuck.

The average() Function
3.
Let’s create the average() function that will compute an average recursively. This is something you may not have seen before, so we will walk you through it.

The average() function will contain a helper function called avg_helper() that will be responsible for implementing a loop to compute an average.

Create a function called avg_helper() That accepts the following three parameters:

curr_count: represents the current count of elements.
itr: represents the collection.
curr_sum: represents the current running total of elements in the collection.
4.
We want avg_helper() to implement the following loop recursively:

curr_count = 0
curr_sum = 0
for i in iterable:
  curr_sum += i
  curr_count += 1

Copy to Clipboard

In our case, curr_sum will be provided from the function call. To obtain the next value in an iterable (if there is one), we have to use next(). If there are no more elements to obtain from the iterable, next() should return the string “null”. The next() function is called like so:

next(iterable, default_value) 

In your avg_helper() function, do the following:

Use next() to obtain the next value in the iterable. Set this value to a variable called next_num. Add this value to curr_sum.
Increment the counter, curr_count, by one.
In the next task, we will see how to handle "null" values.

5.
A recursive function performs the next iteration in the loop by making a call to itself and terminates the loop when a base case is reached.

In our case, the loop should terminate when all the elements in the iterable are processed; i.e., next() returns "null". When next() returns "null", avg_helper() should compute the average and return that value.

Implement this functionality inavg_helper(). To do this:

Increment curr_count by one on each iteration.
Return average if next() returns "null" (use an if statement)
6.
If "null" is not returned, that means there are still more values to add up.

The next iteration of the loop is computed by making a call to avg_helper() with the new curr_count and curr_sum supplied.

Call avg_helper() in the proper location and return the value.

7.
Typically, recursive functions follow this style:

def recursive_function():
  # Base Case
  # Computation
  # Recursive call

Copy to Clipboard

If your code is not written in this style, refactor your avg_helper() function to match it.

8.
Inside average(), make the initial call to avg_helper() with the proper initial values for curr_count and curr_sum. Return the value found by avg_helper().

Using count() and average()
9.
You will now use your count() and average() functions on data obtained from a CSV file called “1kSalesRec.csv”. This file contains order data from a warehouse.

The fields in this CSV file are:

["Region", "Country", "Item Type", "Sales Channel", "Order Priority", "Order Date", "Order ID", "Ship Date", "Units Sold", "Unit Price", "Unit Cost", "Total Revenue", "Total Cost", "Total Profit"]

Copy to Clipboard

Under the section of code that opens a CSV file and creates a reader object, use your count() function to count the number of orders for the country “Belgium”.

To do this:

Replace count_belgiums = None with your count() function.
Within your count() function call, use the following lambda function:
lambda x: x[1] == "Belgium"

Copy to Clipboard

Recall that a record is read in a list. In this case, Country is the second item in the list (index 1).

What should your second argument be?
10.
Use your average() function to compute the average total profit (index 13) for Portugal. Replace avg_portugal = None with your function call.

To do this:

You first need to use filter() to extract all records with Country “Portugal”
Then you need to use map() to extract the Total Profit (index 13).
Be careful about which order you use filter() and map() in your average() functional call.

Note: the entries in the list that represents the records are all of type string. You must convert them to float by using float().

Congrats!
11.
Fantastic job finishing this project! This was a challenging project where we introduced new material and pushed you to do some challenging analysis. We hope you enjoyed it. If you are looking to do more, you can:

Analyze different parts of 1kSalesRec.csv
Create more higher order functions, such as median() or standard_deviation()
Come up with different ways to calculate the values from tasks nine and ten.
Happy coding!