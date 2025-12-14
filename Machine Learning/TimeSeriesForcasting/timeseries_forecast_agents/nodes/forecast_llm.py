import pandas as pd
import json
from langchain_ollama import ChatOllama
from datetime import datetime, timedelta
from io import StringIO

llm = ChatOllama(model="llama3.2:1b", temperature=0.3)  # Lower temperature for consistency

def forecast_llm_node(state):
    df = pd.read_json(StringIO(state.input_data)).copy()
    last_date = df['date'].iloc[-1]  # Last date in input data
    df.rename(columns={"date": "ds", "sales": "y"}, inplace=True)
    last_date = pd.to_datetime(df['ds'].iloc[-1])
    future_dates = [(last_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 8)]

    prompt = f"Do not write a code. Return JSON only. Do not include any text before or after. Forecast the next {state.forecasting_window} days of sales for the following dates:\n"
    prompt += "\n".join([f"{d}" for d in future_dates])
    prompt += "\n\nBased on this historical data:\n"
    for _, row in df.tail(10).iterrows():  # Use last 10 days for context
        prompt += f"{row['ds']}: {int(row['y'])}\n"
    prompt += "\nReturn ONLY a valid JSON object with exactly 7 dates as keys (YYYY-MM-DD) and sales forecasts as numbers"
    
    
    response = llm.invoke(prompt)
    print("LLM Response:", response.content)  # Debug output
    try:
        forecast = json.loads(response.content.strip())
        forecast = {str(k): float(v) for k, v in forecast.items()}
        # Validate forecast has correct dates
        if set(forecast.keys()) != set(future_dates):
            raise ValueError("LLM forecast dates don't match expected dates")
    except Exception as e:
        forecast = {d: 0.0 for d in future_dates}  # Default forecast with correct dates
        print(f"LLM JSON parsing failed: {str(e)}. Using default forecast (zeros).")
    
    return {**state.model_dump(), "llm_forecast": forecast}