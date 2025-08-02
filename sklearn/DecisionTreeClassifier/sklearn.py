import codecademylib3
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

#https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data
cols = ['name','landmass','zone', 'area', 'population', 'language','religion','bars','stripes','colours',
'red','green','blue','gold','white','black','orange','mainhue','circles',
'crosses','saltires','quarters','sunstars','crescent','triangle','icon','animate','text','topleft','botright']
df= pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data", names = cols)

#variable names to use as predictors
var = [ 'red', 'green', 'blue','gold', 'white', 'black', 'orange', 'mainhue','bars','stripes', 'circles','crosses', 'saltires','quarters','sunstars','triangle','animate']

#Print number of countries by landmass, or continent
print(df['landmass'].value_counts())
print(df.head(10))

#Create a new dataframe with only flags from Europe and Oceania
df_36 = df[df['landmass'].isin([3,6])]
print(df_36.head())

#Print the average vales of the predictors for Europe and Oceania'
print(df_36.groupby('landmass')[var].mean())
#Create labels for only Europe and Oceania
labels = (df['landmass'].isin([3,6])) * 1
print(labels.head())
#Print the variable types for the predictors
print(df_36[var].dtypes)

#Create dummy variables for categorical predictors
data = pd.get_dummies(df[var])
print(data.head())
#Split data into a train and test set
x = data
y = labels
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state =1, test_size = .4) 

#Fit a decision tree for max_depth values 1-20; save the accuracy score in acc_depth
depths = range(1, 21)
acc_depth = []
for depth in depths:
  model = DecisionTreeClassifier(max_depth = depth)
  model.fit(x_train, y_train)
  accuracy = model.score(x_test, y_test)
  acc_depth.append(accuracy)

#Plot the accuracy vs depth
plt.plot(depths, acc_depth)
plt.xlabel('depths')
plt.ylabel('accuracy of depth')
plt.grid(True)
plt.show()
#Find the largest accuracy and the depth this occurs
print(np.max(acc_depth))
zipped = list(zip(depths, acc_depth))
zip_array = np.array(zipped)
max_acc = np.argmax(zip_array[:, 1])
best_depth = zip_array[max_acc,0]
print(best_depth)

#Refit decision tree model with the highest accuracy and plot the decision tree
best_tree = DecisionTreeClassifier(max_depth = best_depth)
best_tree.fit(x_train,y_train)
plt.figure(figsize= (10,20))
tree.plot_tree(best_tree)
plt.show()
best_tree.score(x_test,y_test)


#Create a new list for the accuracy values of a pruned decision tree.  Loop through
#the values of ccp and append the scores to the list
path = best_tree.cost_complexity_pruning_path(x_train, y_train)
print(path)
ccp_alphas, impurities = path.ccp_alphas, path.impurities
acc_pruned = []

for ccp_alpha in ccp_alphas:
  model_pruned = DecisionTreeClassifier(max_depth=best_depth, ccp_alpha=ccp_alpha)
  model_pruned.fit(x_train, y_train)  # Fit the model on training data
  accuracy_pruned = model_pruned.score(x_test, y_test)  # Evaluate on test data
  acc_pruned.append(accuracy_pruned) 

#Plot the accuracy vs ccp_alpha
# Step 3: Plot Accuracy vs. ccp_alpha
plt.figure(figsize=(8, 6))
plt.plot(ccp_alphas, acc_pruned)
plt.xlabel('ccp_alpha')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. ccp_alpha for Pruned Decision Trees')
plt.grid(True)
plt.show()


#Find the largest accuracy and the ccp value this occurs
# Step 4: Find the largest accuracy and the corresponding ccp_alpha
best_ccp_alpha = ccp_alphas[np.argmax(acc_pruned)]  # Find the alpha with the highest accuracy
print(f"Best ccp_alpha: {best_ccp_alpha}")
print(f"Best Pruned Accuracy: {max(acc_pruned)}")


#Fit a decision tree model with the values for max_depth and ccp_alpha found above
new_tree = DecisionTreeClassifier(max_depth = best_depth,ccp_alpha = best_ccp_alpha)
new_tree.fit(x_train, y_train)
plt.figure(figsize=(10,15))
tree.plot_tree(new_tree)
plt.show()
final_accuracy = new_tree.score(x_test, y_test)
print(f"Accuracy of the final pruned tree: {final_accuracy:.2f}")

feature_names = x.columns  # because you used pd.get_dummies
class_names = ['Europe', 'Oceania']  # 0 = Europe, 1 = Oceania

# Plot the tree with labels
plt.figure(figsize=(20, 10))
tree.plot_tree(
    new_tree, 
    feature_names=feature_names, 
    class_names=class_names, 
    filled=True, 
    rounded=True,
    fontsize=8
)
plt.title("Final Pruned Decision Tree with Labels")
plt.show()