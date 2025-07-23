import numpy as np
import scipy.stats as stats

# Step 1: Set rate parameter (expected defects per day)
lam = 7

# Step 2: Probability of observing exactly 7 defects
prob_exact_lam = stats.poisson.pmf(lam, lam)
print("P(exactly 7 defects):", prob_exact_lam)

# Step 3: Probability of having 4 or fewer defects
prob_good_day = stats.poisson.cdf(4, lam)
print("P(4 or fewer defects):", prob_good_day)

# Step 4: Probability of more than 9 defects
prob_bad_day = 1 - stats.poisson.cdf(9, lam)
print("P(more than 9 defects):", prob_bad_day)

# Step 5: Simulate a year of defect data
np.random.seed(42)  # for reproducibility
year_defects = np.random.poisson(lam, 365)

# Step 6: Print first 20 values
print("First 20 days of defects:", year_defects[:20])

# Step 7: Expected defects in 365 days
expected_total_defects = lam * 365
print("Expected total defects in a year:", expected_total_defects)

# Step 8: Actual total defects
actual_total_defects = np.sum(year_defects)
print("Actual total defects in a year:", actual_total_defects)

# Step 9: Average number of defects per day
avg_defects = np.mean(year_defects)
print("Average defects per day (simulated):", avg_defects)

# Step 10: Max defects on a single day
max_defects = np.max(year_defects)
print("Max defects on a single day:", max_defects)

# Step 11: P(X >= max_defects)
prob_extreme_day = 1 - stats.poisson.cdf(max_defects - 1, lam)
print(f"P({max_defects} or more defects):", prob_extreme_day)

# Step 12: 90th percentile defect count
percentile_90 = stats.poisson.ppf(0.9, lam)
print("Defects at 90th percentile:", int(percentile_90))

# Step 13: Proportion of days at or above 90th percentile
days_above_90th = np.sum(year_defects >= percentile_90)
proportion_above_90th = days_above_90th / len(year_defects)
print("Proportion of days in 90th percentile or higher:", proportion_above_90th)
