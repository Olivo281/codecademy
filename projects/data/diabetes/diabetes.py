import pandas as pd
import numpy as np

# 2. Load the diabetes data and print the first few rows
diabetes_data = pd.read_csv('diabetes.csv')
print("First few rows:")
print(diabetes_data.head())

# 3. Number of columns (features)
num_columns = diabetes_data.shape[1]
print(f"\nNumber of columns: {num_columns}")

# 4. Number of rows (observations)
num_rows = diabetes_data.shape[0]
print(f"Number of rows: {num_rows}")

# 5. Check for null (missing) values in columns
null_counts = diabetes_data.isnull().sum()
print("\nNull values per column:")
print(null_counts)

# 6. Calculate summary statistics to investigate missing or odd values
print("\nSummary statistics:")
print(diabetes_data.describe())

# 7-8. Notice columns with suspicious zeroes (Glucose, BloodPressure, SkinThickness, Insulin, BMI)
# 9. Replace zeroes with NaN in the specified columns
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
diabetes_data[cols_with_zeros] = diabetes_data[cols_with_zeros].replace(0, np.nan)

# 10. Check again for missing values after replacing 0 with NaN
null_counts_after = diabetes_data.isnull().sum()
print("\nMissing values after replacing 0 with NaN:")
print(null_counts_after)

# 11. Print rows with missing values
print("\nRows with missing values:")
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

# 12. (This is more interpretative, but you can start here with a groupby or value_counts)
print("\nMissing data patterns:")
for col in cols_with_zeros:
    missing_count = diabetes_data[diabetes_data[col].isnull()].shape[0]
    print(f"{col}: {missing_count} missing values")

# 13. Check data types of each column
print("\nData types:")
print(diabetes_data.dtypes)

# 14. Print unique values in the 'Outcome' column
print("\nUnique values in Outcome column:")
print(diabetes_data['Outcome'].unique())

# 15. How to resolve data type issue if Outcome is object (string)
# If Outcome is object type and has numeric strings, convert it to int
if diabetes_data['Outcome'].dtype == 'object':
    diabetes_data['Outcome'] = diabetes_data['Outcome'].astype(int)
    print("\nConverted 'Outcome' to int.")

# Verify conversion
print("\nData types after conversion:")
print(diabetes_data.dtypes)
