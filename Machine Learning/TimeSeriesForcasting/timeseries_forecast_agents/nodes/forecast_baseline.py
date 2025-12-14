from prophet import Prophet
import pandas as pd
from datetime import datetime, timedelta
from io import StringIO

def forecast_baseline_node(state):
    df = pd.read_json(StringIO(state.preprocessed_df)).copy()
    df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)
    last_date = pd.to_datetime(df['ds'].iloc[-1])
    future_dates = [(last_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 8)]
    
    model = Prophet()
    model.add_regressor('rolling_mean_7')
    model.fit(df)
    future = pd.DataFrame({
        'ds': future_dates,
        'rolling_mean_7': [df['rolling_mean_7'].iloc[-1]] * 7  # Use last rolling mean for future
    })
    forecast = model.predict(future)
    result = forecast[["ds", "yhat"]].copy()
    # Ensure ds is string type for JSON serialization and downstream validation
    result.loc[:, "ds"] = pd.to_datetime(result["ds"]).dt.strftime("%Y-%m-%d")
    result_series = result.set_index("ds")["yhat"]
    result_series.index = result_series.index.astype(str)
    result = result_series.to_dict()
    return {**state.model_dump(), "baseline_forecast": result}