import pandas as pd

# Assuming the dataframes visits, cart, checkout, purchase are already loaded
# Each dataframe should have columns: 'user_id' and a timestamp column (e.g., 'visit_time', 'cart_time', etc.)

# For example, if not loaded, you might do:
# visits = pd.read_csv('visits.csv')
# cart = pd.read_csv('cart.csv')
# checkout = pd.read_csv('checkout.csv')
# purchase = pd.read_csv('purchase.csv')

# Step 1: Inspect the data
print("Visits head:")
print(visits.head())
print("\nCart head:")
print(cart.head())
print("\nCheckout head:")
print(checkout.head())
print("\nPurchase head:")
print(purchase.head())

# Step 2: Merge visits and cart using left merge on 'user_id'
visits_cart = pd.merge(visits, cart, how='left', on='user_id')
print("\nMerged visits and cart (visits_cart) head:")
print(visits_cart.head())

# Step 3: Length of the merged DataFrame
print(f"\nLength of visits_cart: {len(visits_cart)}")

# Step 4: Count nulls in cart_time (meaning user didn't add to cart)
num_null_cart_time = visits_cart['cart_time'].isnull().sum()
print(f"Number of nulls in cart_time: {num_null_cart_time}")

# Explanation: Nulls in 'cart_time' mean users visited but did not add a t-shirt to their cart.

# Step 5: Calculate percent of users who visited but did NOT put a t-shirt in cart
percent_no_cart = float(num_null_cart_time) / len(visits_cart) * 100
print(f"Percent of users who visited but did NOT put a t-shirt in cart: {percent_no_cart:.2f}%")

# Step 6: Left merge cart and checkout on 'user_id'
cart_checkout = pd.merge(cart, checkout, how='left', on='user_id')
num_null_checkout_time = cart_checkout['checkout_time'].isnull().sum()
percent_no_checkout = float(num_null_checkout_time) / len(cart_checkout) * 100
print(f"\nNumber of nulls in checkout_time: {num_null_checkout_time}")
print(f"Percent of users who put items in cart but did NOT proceed to checkout: {percent_no_checkout:.2f}%")

# Step 7: Merge all four steps (visits, cart, checkout, purchase)
all_data = visits \
    .merge(cart, how='left', on='user_id') \
    .merge(checkout, how='left', on='user_id') \
    .merge(purchase, how='left', on='user_id')

print("\nAll funnel data head:")
print(all_data.head())

# Step 8: Calculate percentage of users who proceeded to checkout but did not purchase
num_checkout_no_purchase = all_data['purchase_time'].isnull().sum()
total_checkout = all_data['checkout_time'].notnull().sum()
percent_checkout_no_purchase = float(num_checkout_no_purchase) / total_checkout * 100

print(f"\nUsers who checked out but did NOT purchase: {num_checkout_no_purchase}")
print(f"Total users who checked out: {total_checkout}")
print(f"Percentage who did not purchase after checkout: {percent_checkout_no_purchase:.2f}%")

# Step 9: Identify weakest step (highest dropout rate)
print("\n--- Dropout Rates at Each Step ---")
# Visitors -> Cart
print(f"Dropout from Visit to Cart: {percent_no_cart:.2f}%")
# Cart -> Checkout
print(f"Dropout from Cart to Checkout: {percent_no_checkout:.2f}%")
# Checkout -> Purchase
print(f"Dropout from Checkout to Purchase: {percent_checkout_no_purchase:.2f}%")

# Step 10: Calculate average time from visit to purchase
# First, convert times to datetime if not already
for col in ['visit_time', 'cart_time', 'checkout_time', 'purchase_time']:
    if all_data[col].dtype == object:
        all_data[col] = pd.to_datetime(all_data[col])

# Calculate time difference column
all_data['time_to_purchase'] = all_data['purchase_time'] - all_data['visit_time']

# Step 11: Examine new column
print("\nTime to purchase for first few users:")
print(all_data['time_to_purchase'].head())

# Step 12: Calculate average time to purchase (ignoring users who did not purchase)
average_time_to_purchase = all_data['time_to_purchase'].mean()
print(f"\nAverage time to purchase: {average_time_to_purchase}")
