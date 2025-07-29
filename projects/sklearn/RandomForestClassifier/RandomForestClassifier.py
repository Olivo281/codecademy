import pandas as pd
import numpy as np
import codecademylib3
import matplotlib.pyplot as plt
import seaborn as sns

#Import models from scikit learn module:
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, RandomForestRegressor
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

col_names = ['age', 'workclass', 'fnlwgt','education', 'education-num', 
'marital-status', 'occupation', 'relationship', 'race', 'sex',
'capital-gain','capital-loss', 'hours-per-week','native-country', 'income']
df = pd.read_csv('adult.data', header=None, names = col_names)

#Distribution of income
# print(df['income'])
# less_50 = df['income'].value_counts(normalize=True)
# print(less_50)

#Clean columns by stripping extra whitespace for columns of type "object"
# print(df.head(5))
string_cols = df.select_dtypes('object').columns
for col in string_cols:
    # print(df[col].head(5).tolist())
    df[col] = df[col].str.strip()
    # print(df[col].head(5).tolist())
# for i in df.columns:
#   print(f'column:', i)
#   print(df[i].loc[0])
#   print(df[i].get_values())
feature_cols = [
    'age', 'workclass', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country'
]

#Create feature dataframe X with feature columns and dummy variables for categorical features
X = pd.get_dummies(df[feature_cols], drop_first = True)
#Create output variable y which is binary, 0 when income is less than 50k, 1 when it is greather than 50k
y = (df['income'] == '>50K').astype(int)

#Split data into a train and test set
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=.2,random_state=99)

#Instantiate random forest classifier, fit and score with default parameters
rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)
print(rfc.score(x_test,y_test))

#Tune the hyperparameter max_depth over a range from 1-25, save scores for test and train set
np.random.seed(0)
accuracy_train=[]
accuracy_test = []
for i in range(1,25):
  rfc2 = RandomForestClassifier(max_depth=i, random_state=1)
  rfc2.fit(x_train,y_train)
  accuracy_train.append(rfc2.score(x_train,y_train))
  accuracy_test.append(rfc2.score(x_test,y_test))

    
#Find the best accuracy and at what depth that occurs
best_accuracy = max(accuracy_test)
best_depth = accuracy_test.index(best_accuracy) + 1
print(best_accuracy)
print(best_depth)

#Plot the accuracy scores for the test and train set over the range of depth values  

# import matplotlib.pyplot as plt
# depths = list(range(1, 25))
# plt.figure(figsize=(10, 6))
# # Plot training accuracy
# plt.plot(depths, accuracy_train, label='Train Accuracy', marker='o')
# Create a list of depth values that match the range you trained on
# Plot test accuracy
# plt.plot(depths, accuracy_test, label='Test Accuracy', marker='s')
# # Label the plot
# plt.xlabel('max_depth')
# plt.ylabel('Accuracy')
# plt.title('Random Forest Accuracy vs. max_depth')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# plt.show()

#Save the best random forest model and save the feature importances in a dataframe
best_rf = RandomForestClassifier(max_depth=best_depth)
best_rf.fit(x_train,y_train)
importances = best_rf.feature_importances_
feature_importances = pd.DataFrame({
    'feature': x_train.columns,
    'importance': importances
})

# Sort by importance descending
feature_importances = feature_importances.sort_values(by='importance', ascending=False)

# Print top 5 features
print(feature_importances.head(5))
#Create two new features, based on education and native country
education_mapping = {
    'Preschool': 'HS-or-less',
    '1st-4th': 'HS-or-less',
    '5th-6th': 'HS-or-less',
    '7th-8th': 'HS-or-less',
    '9th': 'HS-or-less',
    '10th': 'HS-or-less',
    '11th': 'HS-or-less',
    '12th': 'HS-or-less',
    'HS-grad': 'HS-or-less',
    'Some-college': 'College',
    'Assoc-acdm': 'College',
    'Assoc-voc': 'College',
    'Bachelors': 'College',
    'Masters': 'Masters+',
    'Doctorate': 'Masters+',
    'Prof-school': 'Masters+'
}

# Create new column
df['education_bin'] = df['education'].map(education_mapping)
df['native_bin'] = df['native-country'].apply(lambda x: 'United-States' if x == 'United-States' else 'Other')

feature_cols = ['age',
       'capital-gain', 'capital-loss', 'hours-per-week', 'sex', 'race','education_bin']
#Use these two new additional features and recreate X and test/train split
# Convert categorical variables to dummy variables
X = pd.get_dummies(df[feature_cols], drop_first=True)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=97)

#Find the best max depth now with the additional two features
from sklearn.ensemble import RandomForestClassifier

# Empty lists to store accuracy scores
accuracy_train = []
accuracy_test = []
print(rfc.get_params())
# Loop over max_depth values from 1 to 25
for depth in range(1, 26):
    # Instantiate RandomForest with current max_depth
    rfc = RandomForestClassifier(max_depth=depth, random_state=99)
    
    # Fit the model
    rfc.fit(X_train, y_train)
    
    # Save training and test accuracy
    accuracy_train.append(rfc.score(X_train, y_train))
    accuracy_test.append(rfc.score(X_test, y_test))

# Find the max accuracy and corresponding depth on test data
best_accuracy = max(accuracy_test)
best_depth = accuracy_test.index(best_accuracy) + 1  # +1 because index starts at 0, but depths start at 1

print(f'Best Test Accuracy: {best_accuracy:.4f} at max_depth = {best_depth}')


depths = list(range(1, 26))
plt.figure(figsize=(10, 6))
plt.plot(depths, accuracy_train, label='Train Accuracy', marker='o')
plt.plot(depths, accuracy_test, label='Test Accuracy', marker='s')
plt.xlabel('max_depth')
plt.ylabel('Accuracy')
plt.title('Random Forest Accuracy vs. max_depth (with binned features)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



