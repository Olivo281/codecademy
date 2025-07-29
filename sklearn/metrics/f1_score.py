from sklearn.metrics import f1_score, precision_score, recall_score

# Ground truth (actual labels)
y_true = [0, 1, 1, 1, 0, 1, 0, 0, 1, 0]

# Model predictions
y_pred = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]

# Calculate individual metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"F1 Score:  {f1:.2f}")
