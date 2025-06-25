Using the Helper Function
1.
In script.py, there are two things preloaded for you:

heart_img: a NumPy array representing a 7x7 matrix of RGB values
show_image(): a helper function that will allow you to show images easily throughout your project
We are going to use show_image() to reveal the photo heart_img represents. Before we do so, let’s go over the functionality of show_image().

show_image() takes in two parameters:

image: a NumPy array of RGB values
name_identifier: a string to title your photo (this will make it easy to keep track of what is being plotted throughout your project)
Use show_image() to plot heart_img with the title "Heart Image". If you get stuck, click the hint for help.

2.
You should now see the following plot in the web browser:

A 7x7 pixel grayscale image of a heart

Can you figure out how the NumPy array heart_img creates that image you see? Take some time to think.

Notice that heart_img is a 7x7 matrix and that the heart image itself is 7x7 pixels. Using show_image(), we mapped each value in heart_img to a 7x7 square matrix with grayscale colors that range from 0 (black) to 255 (white).

With this in mind, what are the heart_img values of the following sections of the heart image we see?

(6, 6) — bottom right
(3, 3) — center
(1, 3) — right below top center
Click the answer to see the answers!

Image Transformations
3.
Now that we understand how a NumPy array maps to an image let’s do some fun image transformations!

Since our image is a matrix, we can do transformations based on linear algebra.

First, let’s invert the colors of our heart image.

Create a new variable called inverted_heart_img that subtracts each value in heart_img from 255.
Show inverted_heart_img with the plot title “Inverted Heart Image.”
4.
You should now see the following plot in the web browser:

Photo of 7x7 pixel grayscale heart that is inverted in color from the previous image

Notice that the white pixels are now black, the black pixels are now white, while the gray pixels are the same since 255-(255/2) = 255/2

Let’s do another image transformation. This time let’s plot a rotation of heart_img.

Create a new variable called rotated_heart_img that swaps the rows and columns of heart_img.
Show rotated_heart_img with the plot title “Rotated Heart Image.”
5.
You should now see the following plot in the web browser:

A 7x7 pixel grayscale image of a rotated heart

The rows of heart_img have now become the columns of rotated_heart_img as we plotted the transpose of heart_img.

Let’s dive into some more complicated operations next!

More Advanced Operations
6.
Below the comment # Random Image, we have the following variable:

random_img = np.random.randint(0,255, (7,7))

Copy to Clipboard

Plot that image using show_image() with the title “Random Image.”

7.
We want to solve for the matrix that creates heart_img given the following equation:

r
a
n
d
o
m
_
i
m
g
⋅
x
=
h
e
a
r
t
_
i
m
g
random_img⋅x=heart_img
Create a variable called x that is the solution to this equation. If you are not sure how to do this, check the hint for some guidance.

Plot x using show_image() with the title “x.”

8.
Create a variable called solved_heart_img that is equal to the product of random_img and x.

Plot solved_heart_img with the plot title “Solved Heart Image.”

What image do you see in the web browser?

Extra
9.
Congrats! You have finished your exploration of image transformations with NumPy and linear algebra. If you want to continue the fun, here are some more things you can try:

Create a new shape with a NumPy array.
Transform your image with a permutation matrix.
Change the color scheme from grayscale. Check the cmap parameter of the imshow() function.
Create a complicated image with more pixels and/or a shape that is not a square matrix.
These are just some of the things you can do. Happy coding!