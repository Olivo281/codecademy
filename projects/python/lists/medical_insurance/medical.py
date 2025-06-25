names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Step 1: Append new individual
names.append("Priscilla")
insurance_costs.append(8320.0)

# Step 2: Create medical_records using zip()
medical_records = list(zip(insurance_costs, names))

# Step 3: Print medical_records
print("Medical Records:", medical_records)

# Step 4: Count medical records
num_medical_records = len(medical_records)

# Step 5: Print number of records
print(f"There are {num_medical_records} medical records.\n")

# Step 6: Get first record
first_medical_record = medical_records[0]

# Step 7: Print first record
print(f"Here is the first medical record: {first_medical_record}\n")

# Step 8: Sort records by insurance cost
medical_records.sort()

# Step 9: Print sorted records
print(f"Here are the medical records sorted by insurance cost: {medical_records}\n")

# Step 10: Get three cheapest
cheapest_three = medical_records[:3]

# Step 11: Print cheapest
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}\n")

# Step 12: Get three most expensive
priciest_three = medical_records[-3:]

# Step 13: Print priciest
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}\n")

# Step 14: Count how many times "Paul" appears
occurrences_paul = names.count("Paul")

# Step 15: Print occurrences of Paul
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.\n")

# Extra: Sort alphabetically by name
records_by_name = list(zip(names, insurance_costs))
records_by_name.sort()
print(f"Medical records sorted alphabetically by name: {records_by_name}\n")

# Extra: Get middle five records (index 3 to 7)
middle_five_records = medical_records[3:8]
print(f"The middle five medical records by cost: {middle_five_records}")
