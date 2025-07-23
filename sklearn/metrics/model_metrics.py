import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    r2_score,
    mean_absolute_percentage_error,
    explained_variance_score
)

# Example actual and predicted values
actual = np.array([3.0, -0.5, 2.0, 7.0])
predicted = np.array([2.5, 0.0, 2.0, 8.0])

def evaluate_model(y_true, y_pred):
    print("🔍 Model Evaluation Metrics with Explanations\n")

    # 1️⃣ Mean Squared Error (MSE)
    mse = mean_squared_error(y_true, y_pred)
    print(f"📐 Mean Squared Error (MSE): {mse:.4f}")
    print("    → Formula: MSE = (1/n) * Σ(y_pred - y_actual)²")
    print("    → Use: Penalizes large errors more heavily (squared). Useful in regression.")
    print("    → Lower is better.\n")

    # 2️⃣ Root Mean Squared Error (RMSE)
    rmse = np.sqrt(mse)
    print(f"📐 Root Mean Squared Error (RMSE): {rmse:.4f}")
    print("    → Formula: RMSE = √MSE")
    print("    → Use: Similar to MSE, but in same units as target. Easier to interpret.")
    print("    → Lower is better.\n")

    # 3️⃣ Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_true, y_pred)
    print(f"📐 Mean Absolute Error (MAE): {mae:.4f}")
    print("    → Formula: MAE = (1/n) * Σ|y_pred - y_actual|")
    print("    → Use: More robust to outliers than MSE. Easier to interpret.")
    print("    → Lower is better.\n")

    # 4️⃣ R² Score (Coefficient of Determination)
    r2 = r2_score(y_true, y_pred)
    print(f"📐 R² Score: {r2:.4f}")
    print("    → Formula: R² = 1 - (SS_res / SS_tot)")
    print("    → Use: Measures % of variance explained by model.")
    print("    → 1.0 is perfect, 0.0 means no better than mean, negative means worse.\n")

    # 5️⃣ Mean Absolute Percentage Error (MAPE)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    print(f"📐 Mean Absolute Percentage Error (MAPE): {mape:.4%}")
    print("    → Formula: MAPE = (1/n) * Σ(|y_pred - y_actual| / |y_actual|)")
    print("    → Use: Good when you care about relative (%) error.")
    print("    → Lower % is better. Sensitive to small true values (div/zero risk).\n")

    # 6️⃣ Explained Variance Score
    evs = explained_variance_score(y_true, y_pred)
    print(f"📐 Explained Variance Score: {evs:.4f}")
    print("    → Formula: 1 - Var(residuals) / Var(actual)")
    print("    → Use: Measures how well predictions capture variability.")
    print("    → Close to 1 means model explains most of the variance.\n")

    # Return dictionary (optional)
    return {
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2,
        "MAPE": mape,
        "Explained Variance": evs
    }

if __name__ == "__main__":
    metrics = evaluate_model(actual, predicted)