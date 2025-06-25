import pandas as pd
census = pd.read_csv('census_data.csv', index_col=0)
print("First 5 rows:")
print(census.head())

# 2. (Review done by inspecting output from above)

# 3. Print data types of each column
print("\nData types:")
print(census.dtypes)

# 4. Print unique values in birth_year column (currently str)
print("\nUnique birth_year values:")
print(census['birth_year'].unique())

# 5. Replace missing value (assumed to be something like '?', '', or 'missing') with 1967
# Replace a specific placeholder — adjust based on actual missing value in data

# Example if missing value is '?':
census['birth_year'] = census['birth_year'].replace('?', '1967')

# Or if missing value is empty string:
# census['birth_year'] = census['birth_year'].replace('', '1967')

print("\nbirth_year unique values after replacement:")
print(census['birth_year'].unique())

# 6. Change datatype of birth_year from str to int
census['birth_year'] = census['birth_year'].astype(int)
print("\nData types after conversion:")
print(census.dtypes)

# 7. Print average birth year of respondents
avg_birth_year = census['birth_year'].mean()
print(f"\nAverage birth year: {avg_birth_year:.2f}")

# 8. Convert higher_tax to ordered categorical variable with specified order
tax_order = ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']
census['higher_tax'] = pd.Categorical(census['higher_tax'], categories=tax_order, ordered=True)
print("\nUnique values of higher_tax after ordering:")
print(census['higher_tax'].unique())

# 9. Label encode higher_tax and print the median
# First convert categories to codes (0 to 4)
census['higher_tax_code'] = census['higher_tax'].cat.codes
median_higher_tax = census['higher_tax_code'].median()
print(f"\nMedian code for higher_tax: {median_higher_tax}")

# 10. One-Hot Encode marital_status
marital_dummies = pd.get_dummies(census['marital_status'], prefix='marital')
census_with_dummies = pd.concat([census, marital_dummies], axis=1)
print("\nFirst five rows with marital_status One-Hot Encoded:")
print(census_with_dummies.head())

# 11. Further suggestions (no code, but ideas)
# - Label encode marital_status: census['marital_code'] = census['marital_status'].astype('category').cat.codes
# - Create age_group based on birth_year (e.g., 25-30, 31-35) using pd.cut, then label encode age_group
