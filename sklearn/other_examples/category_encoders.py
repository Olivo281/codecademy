import numpy as np
import pandas as pd
import category_encoders as ce

# Explanation of category_encoders
# - BinaryEncoder: Converts categorical variables into binary representation. Useful for high-cardinality categorical data.
# - TargetEncoder: Encodes categorical variables based on the mean of the target variable. Suitable for supervised learning.
# - OneHotEncoder: Converts categorical variables into a one-hot numeric array. Useful when there are few unique categories.
# - HashingEncoder: Uses the hashing trick to encode categorical variables, reducing dimensionality and memory usage.
# - HelmertEncoder: Encodes categorical data by showing comparisons between levels. Useful for ordinal categories.
# - SumEncoder: A contrast encoding method that helps compare different category levels to an overall effect.
# - PolynomialEncoder: Encodes categories with polynomial contrasts. Often used in statistical modeling.

# Generate sample data
np.random.seed(42)
data = {
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=10),
    'Target': np.random.randint(0, 2, size=10)
}
df = pd.DataFrame(data)

# Applying BinaryEncoder
binary_encoder = ce.BinaryEncoder(cols=['Category'])
df_binary = binary_encoder.fit_transform(df)
print("Binary Encoder:\n", df_binary)

# Applying TargetEncoder
target_encoder = ce.TargetEncoder(cols=['Category'])
df_target = df.copy()
df_target['Category'] = target_encoder.fit_transform(df['Category'], df['Target'])
print("\nTarget Encoder:\n", df_target)

# Applying OneHotEncoder
onehot_encoder = ce.OneHotEncoder(cols=['Category'])
df_onehot = onehot_encoder.fit_transform(df)
print("\nOneHot Encoder:\n", df_onehot)

# Applying HashingEncoder
hashing_encoder = ce.HashingEncoder(cols=['Category'], n_components=4)
df_hashing = hashing_encoder.fit_transform(df)
print("\nHashing Encoder:\n", df_hashing)

# Applying HelmertEncoder
helmert_encoder = ce.HelmertEncoder(cols=['Category'])
df_helmert = helmert_encoder.fit_transform(df)
print("\nHelmert Encoder:\n", df_helmert)

# Applying SumEncoder
sum_encoder = ce.SumEncoder(cols=['Category'])
df_sum = sum_encoder.fit_transform(df)
print("\nSum Encoder:\n", df_sum)

# Applying PolynomialEncoder
poly_encoder = ce.PolynomialEncoder(cols=['Category'])
df_poly = poly_encoder.fit_transform(df)
print("\nPolynomial Encoder:\n", df_poly)