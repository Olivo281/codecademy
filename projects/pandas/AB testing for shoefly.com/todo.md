lyzing Ad Sources
1.
Examine the first few rows of ad_clicks.

2.
Your manager wants to know which ad platform is getting you the most views.

How many views (i.e., rows of the table) came from each utm_source?

3.
If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.

4.
We want to know the percent of people who clicked on ads from each utm_source.

Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.

5.
Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

Save your results to the variable clicks_pivot.

6.
Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

Was there a difference in click rates for each source?

Analyzing an A/B Test
7.
The column experimental_group tells us whether the user was shown Ad A or Ad B.

Were approximately the same number of people shown both ads?

8.
Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

9.
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.

10.
For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.

11.
Compare the results for A and B. What happened over the course of the week?

Do you recommend that your company use Ad A or Ad B?