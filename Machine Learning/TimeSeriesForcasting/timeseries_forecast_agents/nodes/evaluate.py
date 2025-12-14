from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

def evaluate_node(state):
    baseline = state.baseline_forecast
    llm = state.llm_forecast
    ground_truth = state.ground_truth
    
    def evaluate(predictions):
        y_true, y_pred = [], []
        # Debug: Print available dates
        print("Ground Truth Dates:", list(ground_truth.keys()))
        print("Prediction Dates:", list(predictions.keys()))
        for d in ground_truth:
            if d in predictions:
                y_true.append(ground_truth[d])
                y_pred.append(predictions[d])
        if not y_true:
            print("No overlapping dates found for evaluation.")
            return {"rmse": float("inf"), "mae": float("inf"), "smape": float("inf")}
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(y_true, y_pred)
        smape = np.mean(2 * np.abs(np.array(y_true) - np.array(y_pred)) /
                        (np.abs(np.array(y_true)) + np.abs(np.array(y_pred))) * 100)
        return {"rmse": rmse, "mae": mae, "smape": smape}
    
    return {
        **state.model_dump(),
        "baseline_scores": evaluate(baseline),
        "llm_scores": evaluate(llm)
    }