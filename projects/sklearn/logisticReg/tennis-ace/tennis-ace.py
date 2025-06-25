import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load and investigate the data
tennis = pd.read_csv('tennis_stats.csv')
print(tennis.head())
print(tennis.info())
print(tennis.describe())

# Exploratory Analysis: scatter plots of features vs Winnings
features_to_plot = ['BreakPointsOpportunities', 'Aces', 'DoubleFaults', 'ServiceGamesPlayed', 'FirstServeReturnPointsWon', 'SecondServeReturnPointsWon']

for feature in features_to_plot:
    plt.scatter(tennis[feature], tennis['Winnings'], alpha=0.5)
    plt.title(f'{feature} vs Winnings')
    plt.xlabel(feature)
    plt.ylabel('Winnings')
    plt.show()

# Single feature linear regression
def single_feature_model(feature):
    x = tennis[[feature]]
    y = tennis[['Winnings']]
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
    
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_pred = lr.predict(x_test)
    
    plt.scatter(x_test, y_pred, alpha=0.5)
    plt.title(f'Predicted vs Actual Winnings using {feature}')
    plt.xlabel(feature)
    plt.ylabel('Predicted Winnings')
    plt.show()
    
    score = lr.score(x_test, y_test)
    print(f"Test score using '{feature}':", score)
    return score

print("\nSingle Feature Models:")
scores = {}
for feature in features_to_plot:
    scores[feature] = single_feature_model(feature)

# Best single feature
best_single = max(scores, key=scores.get)
print("\nBest single feature for predicting winnings:", best_single)

# Two-feature models
def two_feature_model(f1, f2):
    x = tennis[[f1, f2]]
    y = tennis[['Winnings']]
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
    
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    score = lr.score(x_test, y_test)
    print(f"Test score using '{f1}' and '{f2}':", score)
    return score

print("\nTwo-Feature Models:")
from itertools import combinations
two_feature_scores = {}
for f1, f2 in combinations(features_to_plot, 2):
    score = two_feature_model(f1, f2)
    two_feature_scores[(f1, f2)] = score

best_two = max(two_feature_scores, key=two_feature_scores.get)
print("\nBest two features for predicting winnings:", best_two)

# Multiple feature model
print("\nMultiple Feature Model:")
x_features = tennis[features_to_plot]
y_winnings = tennis[['Winnings']]
x_train, x_test, y_train, y_test = train_test_split(x_features, y_winnings, train_size=0.8)

multiple = LinearRegression()
multiple.fit(x_train, y_train)
score = multiple.score(x_test, y_test)
print("Multiple feature model test score:", score)
print("Feature Coefficients:", list(zip(features_to_plot, multiple.coef_[0])))

