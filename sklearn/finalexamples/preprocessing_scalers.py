import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OrdinalEncoder, LabelEncoder

# Data Preprocessing Explanation
# - StandardScaler: Standardizes features by removing the mean and scaling to unit variance.
# - MinMaxScaler: Scales features to a fixed range (0 to 1) to maintain proportional relationships.
# - OrdinalEncoder: Encodes categorical variables with inherent order (e.g., low, medium, high).
# - LabelEncoder: Encodes categorical variables without considering order, assigning unique integer values.

# Generate sample data
np.random.seed(42)
data = {
    'Feature1': np.random.randn(10),
    'Feature2': np.random.rand(10) * 100,
    'Category': np.random.choice(['Low', 'Medium', 'High'], size=10)
}
df = pd.DataFrame(data)

# Applying StandardScaler
scaler = StandardScaler()
df[['Feature1', 'Feature2']] = scaler.fit_transform(df[['Feature1', 'Feature2']])

# Applying MinMaxScaler
minmax_scaler = MinMaxScaler()
df[['Feature1', 'Feature2']] = minmax_scaler.fit_transform(df[['Feature1', 'Feature2']])

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]
def min_max_normalize(lst):
  minimum = min(lst)
  maximum = max(lst)
  normalized = []
  for i in lst:
   normalized.append((i-minimum)/(maximum-minimum))
  return normalized

print(min_max_normalize(release_dates))

# Applying OrdinalEncoder
encoder = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
df['Category'] = encoder.fit_transform(df[['Category']])

# Applying LabelEncoder
label_encoder = LabelEncoder()
df['Category_Label'] = label_encoder.fit_transform(df['Category'])

# Display preprocessed data
print(df)
