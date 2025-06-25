import pandas as pd

# Step 1: Examine the first few rows of ad_clicks
print("ad_clicks head:")
print(ad_clicks.head())

# Step 2: Count how many views came from each utm_source
views_by_source = ad_clicks['utm_source'].value_counts()
print("\nNumber of views from each utm_source:")
print(views_by_source)

# Step 3: Create a new column 'is_click' (True if ad_click_timestamp not null)
ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()
print("\nAdded 'is_click' column:")
print(ad_clicks.head())

# Step 4: Group by utm_source and is_click, count user_id
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
print("\nClicks by source and is_click:")
print(clicks_by_source)

# Step 5: Pivot the data: columns = is_click (True/False), index = utm_source, values = user_id counts
clicks_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id').reset_index()
clicks_pivot.columns.name = None  # clean up columns names
print("\nPivoted clicks data:")
print(clicks_pivot)

# Step 6: Calculate percent_clicked for each utm_source
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100
print("\nClicks pivot with percent_clicked:")
print(clicks_pivot)

# Step 7: Check how many people were shown Ad A and Ad B
ad_counts = ad_clicks['experimental_group'].value_counts()
print("\nNumber of people shown each ad:")
print(ad_counts)

# Step 8: Calculate the percentage of users who clicked on each ad group
clicks_by_experiment = ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
clicks_pivot_exp = clicks_by_experiment.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()
clicks_pivot_exp['percent_clicked'] = clicks_pivot_exp[True] / (clicks_pivot_exp[True] + clicks_pivot_exp[False]) * 100
print("\nClick rates by experimental group:")
print(clicks_pivot_exp)

# Step 9: Create separate DataFrames for A and B groups
a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']

# Step 10: Calculate percent of users who clicked on ad by day for both groups
a_clicks_by_day = a_clicks.groupby(['day', 'is_click'])['user_id'].count().reset_index()
a_pivot = a_clicks_by_day.pivot(index='day', columns='is_click', values='user_id').reset_index()
a_pivot['percent_clicked'] = a_pivot[True] / (a_pivot[True] + a_pivot[False]) * 100

b_clicks_by_day = b_clicks.groupby(['day', 'is_click'])['user_id'].count().reset_index()
b_pivot = b_clicks_by_day.pivot(index='day', columns='is_click', values='user_id').reset_index()
b_pivot['percent_clicked'] = b_pivot[True] / (b_pivot[True] + b_pivot[False]) * 100

print("\nPercent clicked by day for Ad A:")
print(a_pivot)

print("\nPercent clicked by day for Ad B:")
print(b_pivot)

# Step 11: Compare results for A and B over the week
# You can visually inspect or plot them
print("\nSummary:")
print("Ad A average click rate by day:")
print(a_pivot[['day', 'percent_clicked']])
print("\nAd B average click rate by day:")
print(b_pivot[['day', 'percent_clicked']])

# Optional: Recommend ad based on average click rate
avg_click_a = a_pivot['percent_clicked'].mean()
avg_click_b = b_pivot['percent_clicked'].mean()
print(f"\nAverage click rate for Ad A: {avg_click_a:.2f}%")
print(f"Average click rate for Ad B: {avg_click_b:.2f}%")

if avg_click_a > avg_click_b:
    print("Recommendation: Use Ad A")
else:
    print("Recommendation: Use Ad B")
