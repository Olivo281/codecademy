import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Assume nba_2010 and nba_2014 DataFrames are pre-loaded

# Step 1: Knicks and Nets points in 2010
knicks_pts_10 = nba_2010.loc[nba_2010['fran_id'] == 'Knicks', 'pts']
nets_pts_10 = nba_2010.loc[nba_2010['fran_id'] == 'Nets', 'pts']

# Step 2: Difference in average points
diff_means_2010 = knicks_pts_10.mean() - nets_pts_10.mean()
print(f"Difference in means (2010): {diff_means_2010}")
# Interpretation: If this is close to zero, they are similar; otherwise, likely associated.

# Step 3: Overlapping histograms for 2010
plt.hist(knicks_pts_10, alpha=0.5, label='Knicks', bins=15)
plt.hist(nets_pts_10, alpha=0.5, label='Nets', bins=15)
plt.legend()
plt.title('Points Distribution: Knicks vs Nets (2010)')
plt.xlabel('Points')
plt.ylabel('Frequency')
plt.show()

# Step 4: Repeat for 2014
knicks_pts_14 = nba_2014.loc[nba_2014['fran_id'] == 'Knicks', 'pts']
nets_pts_14 = nba_2014.loc[nba_2014['fran_id'] == 'Nets', 'pts']
diff_means_2014 = knicks_pts_14.mean() - nets_pts_14.mean()
print(f"Difference in means (2014): {diff_means_2014}")

plt.hist(knicks_pts_14, alpha=0.5, label='Knicks', bins=15)
plt.hist(nets_pts_14, alpha=0.5, label='Nets', bins=15)
plt.legend()
plt.title('Points Distribution: Knicks vs Nets (2014)')
plt.xlabel('Points')
plt.ylabel('Frequency')
plt.show()

# Step 5: Boxplots for all teams in 2010
plt.figure(figsize=(12,6))
sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.xticks(rotation=45)
plt.title('Points per Game by Team (2010)')
plt.xlabel('Team')
plt.ylabel('Points per Game')
plt.show()

# Step 6: Contingency table of game_result vs game_location
location_result_freq = pd.crosstab(nba_2010['game_result'], nba_2010['game_location'])
print("Contingency table (counts):")
print(location_result_freq)

# Step 7: Convert to proportions
location_result_proportions = location_result_freq / location_result_freq.sum().sum()
print("\nContingency table (proportions):")
print(location_result_proportions)

# Step 8: Chi-square test and expected frequencies
chi2, p, dof, expected = chi2_contingency(location_result_freq)
print(f"\nChi-square statistic: {chi2}")
print(f"P-value: {p}")
print("Degrees of freedom:", dof)
print("Expected frequencies:")
print(pd.DataFrame(expected, index=location_result_freq.index, columns=location_result_freq.columns))
# Interpretation: If observed frequencies differ significantly from expected, variables may be associated

# Step 9: Covariance between forecast and point_diff
point_diff_forecast_cov = nba_2010[['forecast', 'point_diff']].cov().iloc[0,1]
print(f"\nCovariance between forecast and point_diff: {point_diff_forecast_cov}")

# Step 10: Correlation between forecast and point_diff
point_diff_forecast_corr = nba_2010[['forecast', 'point_diff']].corr().iloc[0,1]
print(f"Correlation between forecast and point_diff: {point_diff_forecast_corr}")

# Step 11: Scatter plot
plt.scatter(nba_2010['forecast'], nba_2010['point_diff'], alpha=0.5)
plt.title('Forecast vs Point Difference (2010)')
plt.xlabel('Forecast Probability of Win')
plt.ylabel('Point Difference')
plt.show()
