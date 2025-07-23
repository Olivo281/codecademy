names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Step 1: Initialize total_cost
total_cost = 0

# Step 2: Add up actual insurance costs
for cost in actual_insurance_costs:
    total_cost += cost

# Step 3: Calculate average cost
average_cost = total_cost / len(actual_insurance_costs)

# Step 4: Print average cost
print("Average Insurance Cost:", average_cost, "dollars.\n")

# Step 5–8: Loop through each individual and compare to average
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]
    print(f"The insurance cost for {name} is {insurance_cost} dollars.")

    if insurance_cost > average_cost:
        print(f"The insurance cost for {name} is above average.\n")
    elif insurance_cost < average_cost:
        print(f"The insurance cost for {name} is below average.\n")
    else:
        print(f"The insurance cost for {name} is equal to the average.\n")

# Step 10: Create updated estimated costs using list comprehension
updated_estimated_costs = [cost * 11 / 10 for cost in estimated_insurance_costs]

# Step 11: Print updated estimated costs
print("Updated Estimated Costs:", updated_estimated_costs)
