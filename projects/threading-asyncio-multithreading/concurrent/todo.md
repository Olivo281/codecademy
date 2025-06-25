
Before diving in, look at the starter code in script.py. There are six functions defined:

cal_average()
This helper function takes in a list of numbers, num, and calculates the average of the numbers within the list. Notice that we have added a time.sleep(1) line before returning the average. This extra second is an added barrier to test the efficiency of each approach, as you will use this helper function in your sequential, threading, and multiprocessing programs.

main_sequential()
This is where you will write your sequential program. The lines s = time.perf_counter() and elapsed = time.perf_counter() - s are there to time your program (they are in the rest of the functions as well.).

cal_average_async()
This helper function is the same as calc_average() except it is an asynchronous function you will use for your async program.

main_async()
This is where you will write your async program.

main_threading()
This is where you will write your threading program.

main_multiprocessing()
This is where you will write your multiprocessing program.

Finally, the code after main_multiprocessing() tests your sequential, async, threading, and multiprocessing functions for you each time your run script.py. There is no need to touch it during the project.

Sequential Approach
2.
In main_sequential(), write a program that calculates the average of three lists sequentially using cal_average() as a helper function.

Your code should go in between s = time.perf_counter() and elapsed = time.perf_counter() - s.

Before running script.py, estimate how long these calculations should take when using main_sequential().

3.
Execute script.py.

How long did it take for the calculation to complete? Does it line up with your estimate?

Async Approach
4.
Now it’s time to try out an async approach.

In the main_aysnc() function, create a variable called tasks and assign it to a list that contains three function calls on list1, list2, and list3 using cal_average_async().

5.
Run each task concurrently. To do this, you will need to:

Use the await keyword
Group your tasks together
Click the hint if you get stuck.

Before running script.py, estimate how long these calculations should take when using main_async().

6.
Run script.py.

How long did it take for the calculation to complete? Does it line up with your estimate?

Threading Approach
7.
Now it’s time to try out the threading approach. Do the following in the main_threading() function:

Create a variable called lists containing three elements: list1, list2, and list3.
Create an empty list called threads.
8.
Still within main_threading(), create a for loop that iterates through range(len(lists)). At each iteration:

Create a thread called x. Your thread should run cal_average() and pass in one of the lists as its argument.
Add each thread to threads.
Start the created thread.
Next, create another for loop. This time loop through each thread in threads. In this for loop, you should join each thread using the .join() method.

Before running script.py, estimate how long these calculations should take when using main_threading().

9.
Run script.py.

How long did it take for the calculation to complete? Does it line up with your estimate?

Multiprocessing Approach
10.
Now it’s time to try out the multiprocessing approach. Within main_multiprocessing(), create a variable called lists containing three elements: list1, list2, and list3.

11.
Still within main_multiprocessing(), create a process object for each list within lists. You can either use a for loop or list comprehension.

12.
Still within main_multiprocessing(), create two separate iterations:

One iteration should go through each process within your processes list and spawn each one using the .start() method.
The second iteration should also go through each process within your processes list and join each one using the .join() method.
Note that you should use two separate iterations to start the processes before you join them together.

Before running script.py, estimate how long these calculations should take when using main_multiprocessing().

13.
Run script.py.

How long did it take for the calculation to complete? Does it line up with your estimate?

Extra
14.
Fantastic job finishing this project! This was a challenging project where we pushed you to do some challenging analysis. We hope you enjoyed it. If you are looking to do more, you can:

Create a new helper function to test the different approaches against.
Add print statements in your helper function. Do they print out in the same order for each approach?
Use a larger dataset instead of a small list, such as data from an Excel worksheet. (You would need to do this on your own computer locally.)
Create a new helper function to test the different approaches against various types of problems, not just finding the average of a list
Happy coding!