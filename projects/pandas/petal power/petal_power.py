import pandas as pd

# Step 1: Load the data into a DataFrame called inventory
inventory = pd.read_csv('inventory.csv')

# Step 2: Inspect the first 10 rows of inventory
print("First 10 rows of inventory:")
print(inventory.head(10))

# Step 3: Select the first 10 rows (Staten Island location) and save to staten_island
staten_island = inventory.iloc[:10]

# Step 4: Select the product_description column from staten_island and save to product_request
product_request = staten_island['product_description']
print("\nProducts at Staten Island location:")
print(product_request)

# Step 5: Select rows where location is 'Brooklyn' and product_type is 'seeds' into seed_request
seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
print("\nSeeds sold at Brooklyn location:")
print(seed_request)

# Step 6: Add 'in_stock' column: True if quantity > 0, else False
inventory['in_stock'] = inventory['quantity'] > 0

# Step 7: Create 'total_value' column = price * quantity
inventory['total_value'] = inventory['price'] * inventory['quantity']

# Step 8: Lambda function to combine product_type and product_description
combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

# Step 9: Create 'full_description' column using combine_lambda
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print("\nInventory with new columns:")
print(inventory.head())
