1.
To start, let’s write a Python function that takes a mathematical function as input and uses the limit definition of a derivative to find the approximate derivate As a refresher the limit definition of the derivative is written out below:

lim
⁡
h
→
0
f
(
x
+
h
)
−
f
(
x
)
h
h→0
lim
​
  
h
f(x+h)−f(x)
​
 
Fill in the body of limit_derivative() so that it returns the following formula from the limit definition of a derivative:

f
(
x
+
h
)
−
f
(
x
)
h
h
f(x+h)−f(x)
​
 
2.
In script.py, there are three functions predefined for you:

f1()— which defines f1(x) = sin(x)
f2()— which defines f2(x) = x4
f3()— which defines f3(x) = x2*log(x)
Note: The default base for the math.log() function is e, so the function defined by f3(x) in script.py is evaluated as:

f
3
(
x
)
=
x
2
∗
l
n
(
x
)
f3(x)=x 
2
 ∗ln(x)
Using the limit_derivative() function, calculate the derivative of f3 at x=1 using the following values of h:

h=2
h=0.1
h=0.00001
Make sure to print out the values. What number does the limit derivative appear to be approaching?

3.
You should have the following output in your terminal:

4.943755299006494
1.1532531756323319
1.0000150000398844

Copy to Clipboard

Verify calculation by evaluating the derivative of f3 mathematically. Click the hint if you get stuck.

4.
Using Python, we see that the value of the limit derivative of f3 approaches 1 at x=1. We then also showed that the derivative is equal to 1 mathematically.

Feel free to do this exercise again with f1 and f2 before we move onto graphing derivatives.

Graphing Approximate Derivative Functions
5.
We are going to graph approximations using plot_approx_deriv(). Before we do anything, let’s go over this function.

It takes one parameter:

f: the function whose derivative is graphed
Inside the function, the following occurs:

The derivate_values are calculated using limit_derivative(). This is done for all x_vals (x values) and h_vals (h values).
After the derivative_values are all calculated, a plot is made for each h in h_vals. This means there will be four different curve approximations.
Let’s say we have a function g. To use plot_approx_deriv(), write the following line of code:

plot_approx_deriv(g)

Copy to Clipboard

6.
Use plot_approx_deriv() to graph limit derivative approximations of f1.

7.
You should see the following plot in the web browser now:

graph of cos(x) and four approximations of cos(x)

Which limit approximations are more accurate and which ones are less accurate? Is there a pattern? Are any of the curves almost an exact match to cos(x)?

8.
Let’s do the same thing with f2. This time, however, we have to update the following line of code:

y_vals = [cos(val) for val in x_vals]

Copy to Clipboard

We graphed cos(x) for the previous exercise since we approximated the derivative of sin(x). However, this time we want to approximate the derivative of x4. Therefore, we have to replace the cos(val) term.

Update this line of code to graph the derivative of x4. Click the hint if you get stuck.

You may also want to comment out plot_approx_deriv(f1).

9.
Use plot_approx_deriv() to graph limit derivative approximations of f2.

Make sure plot_approx_deriv(f1) has been commented out or deleted.

10.
You should see the following plot in the web browser now:

graph of 4x^3 and four approximations of 4x^3

As with the previous graph, this aligns with the limit definition of a derivative. The closer h gets to 0, the closer the derivative function gets to the true derivative curve.

Extensions
11.
Congrats! That concludes our exploration into the limit definition of the derivative using Python. We have approximated derivatives at a point and whole derivative functions using the limit definition. If you would like to continue your exploration, here are some ideas:

Modify plot_approx_deriv() so it uses np.gradient().
Create your own functions and investigate them through plotting and calculating derivatives.
Change the h_vals and/or x_vals to look at a different range or values.
Compare our method of plot_approx_deriv() to plotting using np.gradient()