# 1. Create an empty dictionary called medical_costs.
medical_costs = {}

# 2. Add Marina and Vinay with their insurance costs.
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# 3. Add Connie, Isaac, and Valentina in one line.
medical_costs.update({
    "Connie": 8886.0,
    "Isaac": 16444.0,
    "Valentina": 6420.0
})

# 4. Print medical_costs
print("Medical costs:", medical_costs)

# 5. Correct Vinay's insurance cost and print updated dictionary
medical_costs["Vinay"] = 3325.0
print("Updated medical costs:", medical_costs)

# 6. Calculate total_cost by summing all insurance costs
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost

# 7. Calculate average_cost and print it
average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")

# 8. Create two lists: names and ages
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

# 9. Create zipped_ages by zipping names and ages
zipped_ages = zip(names, ages)

# 10. Create dictionary names_to_ages using list comprehension
names_to_ages = {name: age for name, age in zipped_ages}
print("Names to ages:", names_to_ages)

# 11. Use .get() to get Marina's age
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}")

# 12. Create empty dictionary medical_records
medical_records = {}

# 13. Add Marina's medical data
medical_records["Marina"] = {
    "Age": 27,
    "Sex": "Female",
    "BMI": 31.1,
    "Children": 2,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6607.0
}

# 14. Add other patients' medical data
medical_records["Vinay"] = {
    "Age": 24,
    "Sex": "Male",
    "BMI": 26.9,
    "Children": 0,
    "Smoker": "Non-smoker",
    "Insurance_cost": 3325.0
}

medical_records["Connie"] = {
    "Age": 43,
    "Sex": "Female",
    "BMI": 25.3,
    "Children": 3,
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0
}

medical_records["Isaac"] = {
    "Age": 35,
    "Sex": "Male",
    "BMI": 20.6,
    "Children": 4,
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
}

medical_records["Valentina"] = {
    "Age": 52,
    "Sex": "Female",
    "BMI": 18.7,
    "Children": 1,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
}

# 15. Print medical_records
print("Medical records:", medical_records)

# 16. Print Connie's insurance cost
connie_cost = medical_records["Connie"]["Insurance_cost"]
print(f"Connie's insurance cost is {connie_cost} dollars.")

# 17. Remove Vinay from medical_records
medical_records.pop("Vinay", None)

# 18. Iterate through medical_records and print formatted info
for name, record in medical_records.items():
    print(f"{name} is a {record['Age']} year old {record['Sex']} {record['Smoker']} with a BMI of {record['BMI']} and insurance cost of {record['Insurance_cost']}")
