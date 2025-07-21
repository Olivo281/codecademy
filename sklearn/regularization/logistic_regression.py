#No regularization:
from sklearn.linear_model import LogisticRegression
logistic_no_regularization = LogisticRegression(penalty = 'none')

#Lasso (L1): The L1 implementation requires setting the penalty attribute to ‘l1’ and also setting the solver attribute to ‘liblinear’
logistic_lasso = LogisticRegression(penalty = 'l1', solver = 'liblinear', C = ___ )

#l2 or default for logistic regression:
logistic_ridge = LogisticRegression(penalty = 'l2', C = ___ )

#ElasticNet (L1 + L2): The ElasticNet implementation requires setting the penalty attribute to ‘elasticnet’, the solver attribute to ‘saga’, and also specifying the l1_ratio parameter.
logistic_elasticnet = LogisticRegression(penalty = 'elasticnet', solver = 'saga', C = ___, l1_ratio = ___ )