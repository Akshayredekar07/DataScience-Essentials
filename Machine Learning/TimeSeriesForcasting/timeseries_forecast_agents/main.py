import pandas as pd
from graph import build_graph
import json

forecasting_window = 7 # days
df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

input_df = df[-365:-forecasting_window].copy()  # 2017-12-15 to 2017-12-24
ground_truth_df = df[-forecasting_window:].copy()  # 2017-12-25 to 2017-12-31

print("Input Data Dates:", input_df["date"].min(), "to", input_df["date"].max())
print("Ground Truth Dates:", ground_truth_df["date"].min(), "to", ground_truth_df["date"].max())

input_json = input_df.reset_index(drop=True).to_json(orient="records", date_format="iso")
ground_truth = {
    d.strftime("%Y-%m-%d"): float(v)
    for d, v in zip(ground_truth_df["date"], ground_truth_df["sales"])
}

graph = build_graph()
initial_state = {
    "input_data": input_json,
    "ground_truth": ground_truth,
    "preprocessed_df": "",
    "baseline_forecast": {},
    "llm_forecast": {},
    "baseline_scores": {},
    "llm_scores": {},
    "explanation": "",
    "forecasting_window":forecasting_window
}

final_state = graph.invoke(initial_state)

print("\nGround Truth:")
print(final_state["ground_truth"])
print("\nProphet Forecast:")
print(final_state["baseline_forecast"])
print("\nLLM Forecast:")
print(final_state["llm_forecast"])
print("\nEvaluation Scores:")
print("Prophet:", final_state["baseline_scores"])
print("LLM    :", final_state["llm_scores"])
print("\nForecast Comparison Explanation:")
print(final_state["explanation"])

