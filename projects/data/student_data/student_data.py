import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assume students DataFrame is loaded already
students = pd.read_csv('students.csv')
# 1. Inspect first few rows
print("First few rows of data:")
print(students.head())

# 2. Summary statistics for all features
print("\nSummary statistics for all features:")
print(students.describe(include='all'))

# Count how many students live in urban vs rural
print("\nCount of students by address:")
print(students['address'].value_counts())

# 3. Mean of math_grade
mean_grade = students['math_grade'].mean()
print(f"\nMean math grade: {mean_grade}")

# 4. Median of math_grade
median_grade = students['math_grade'].median()
print(f"Median math grade: {median_grade}")

# 5. Mode of math_grade
mode_grade = students['math_grade'].mode()[0]
print(f"Mode math grade: {mode_grade}")

# 6. Range of math_grade
grade_range = students['math_grade'].max() - students['math_grade'].min()
print(f"Range of math grades: {grade_range}")

# 7. Standard deviation of math_grade
std_grade = students['math_grade'].std()
print(f"Standard deviation of math grades: {std_grade}")

# 8. Mean absolute deviation of math_grade
mad_grade = students['math_grade'].mad()
print(f"Mean absolute deviation of math grades: {mad_grade}")

# 9. Histogram of math_grade
sns.histplot(students['math_grade'], bins=20, kde=False)
plt.title('Histogram of Math Grades')
plt.xlabel('Math Grade')
plt.ylabel('Frequency')
plt.show()
plt.clf()

# 10. Boxplot of math_grade
sns.boxplot(x=students['math_grade'])
plt.title('Boxplot of Math Grades')
plt.xlabel('Math Grade')
plt.show()
plt.clf()

# 11. Count of students by mothers' job (Mjob)
print("Counts of mother's job types:")
mjob_counts = students['Mjob'].value_counts()
print(mjob_counts)

# Most common Mjob
most_common_mjob = mjob_counts.idxmax()
print(f"Most common mother's job: {most_common_mjob}")

# 12. Proportion of students by mother's job
mjob_proportions = students['Mjob'].value_counts(normalize=True)
print("\nProportions of mother's job types:")
print(mjob_proportions)

# Proportion of mothers in health
health_proportion = mjob_proportions.get('health', 0)
print(f"Proportion of mothers working in health: {health_proportion}")

# 13. Bar chart of Mjob counts
sns.countplot(x='Mjob', data=students, order=mjob_counts.index)
plt.title("Counts of Mother's Jobs")
plt.xlabel("Mother's Job")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
plt.clf()

# 14. Pie chart of Mjob proportions
plt.pie(mjob_counts, labels=mjob_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Mother's Jobs")
plt.axis('equal')  # Equal aspect ratio to make pie circular
plt.show()

# 15. Further exploration suggestion:
print("\nFurther exploration ideas:")
print("- Analyze 'address' with counts and proportion (urban vs rural).")
print("- Visualize 'absences' with histogram or boxplot.")
print("- Explore 'Fjob' counts and proportions similarly to 'Mjob'.")
