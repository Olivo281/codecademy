model = GridSearchCV(estimator = Ridge(),param_grid = tuned_parameters,scoring = 'neg_mean_squared_error', cv = 5, return_train_score = True)
print(model.best_score_)
print(model.best_params_)
print(model.best_estimator_)
best_score_ = how well the model did
best_params_ = what setting got the best performance
best_estimator_ = the trained model with that setting

