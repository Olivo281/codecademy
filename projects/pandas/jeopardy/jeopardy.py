import pandas as pd
import re

# Display full column content
pd.set_option('display.max_colwidth', None)

# Step 2: Load the data
jeopardy = pd.read_csv('jeopardy.csv')

# Clean column names by stripping whitespace
jeopardy.columns = jeopardy.columns.str.strip()

# Print original columns and first few rows to understand the data
print("Columns:")
print(jeopardy.columns)
print("\nFirst 5 rows:")
print(jeopardy.head())

# Step 3 & 4: Define a robust filter function to find questions containing all words
def filter_questions_robust(df, words):
    filtered_df = df.copy()
    for word in words:
        # Regex pattern for whole word, case-insensitive
        pattern = rf'\b{re.escape(word)}\b'
        filtered_df = filtered_df[filtered_df['Question'].str.contains(pattern, case=False, na=False, regex=True)]
    return filtered_df

# Example test
test_words = ["King", "England"]
filtered = filter_questions_robust(jeopardy, test_words)
print(f"\nNumber of questions containing {test_words}: {len(filtered)}")
print(filtered['Question'].head())

# Step 5: Convert the "Value" column to floats
# Remove $ and commas, convert to numeric, errors to NaN
jeopardy['Value_float'] = jeopardy['Value'].str.replace('[\$,]', '', regex=True)
jeopardy['Value_float'] = pd.to_numeric(jeopardy['Value_float'], errors='coerce')

print("\nSample 'Value' to 'Value_float' conversion:")
print(jeopardy[['Value', 'Value_float']].head())

# Calculate average value of questions containing the word "King"
king_questions = filter_questions_robust(jeopardy, ["King"])
print(f"\nAverage value of questions containing 'King': {king_questions['Value_float'].mean()}")

# Step 6: Function to count unique answers
def unique_answer_counts(df):
    return df['Answer'].value_counts()

# Count answers for "King" questions
king_answer_counts = unique_answer_counts(king_questions)
print("\nMost common answers for 'King' questions:")
print(king_answer_counts.head())

# Additional exploration example:
# Count how many questions contain "Computer" from 1990s vs 2000s
jeopardy['Air Date'] = pd.to_datetime(jeopardy['Air Date'])
questions_90s = jeopardy[(jeopardy['Air Date'].dt.year >= 1990) & (jeopardy['Air Date'].dt.year < 2000)]
questions_2000s = jeopardy[(jeopardy['Air Date'].dt.year >= 2000) & (jeopardy['Air Date'].dt.year < 2010)]

computer_90s = filter_questions_robust(questions_90s, ["Computer"])
computer_2000s = filter_questions_robust(questions_2000s, ["Computer"])

print(f"\nNumber of 'Computer' questions in the 1990s: {len(computer_90s)}")
print(f"Number of 'Computer' questions in the 2000s: {len(computer_2000s)}")
