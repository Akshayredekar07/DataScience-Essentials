from langgraph.graph import StateGraph
from nodes.preprocess import preprocess_node
from nodes.forecast_baseline import forecast_baseline_node
from nodes.forecast_llm import forecast_llm_node
from nodes.evaluate import evaluate_node
from nodes.explain import explain_node
from pydantic import BaseModel
from typing import Dict

class StateSchema(BaseModel):
    input_data: str               # JSON string of input time series
    preprocessed_df: str          # JSON string of preprocessed DataFrame
    baseline_forecast: Dict[str, float]  # Date strings to forecasted values
    llm_forecast: Dict[str, float]      # Date strings to forecasted values
    ground_truth: Dict[str, float]      # Date strings to actual values
    baseline_scores: Dict[str, float]   # Metrics for baseline
    llm_scores: Dict[str, float]        # Metrics for LLM
    explanation: str                    # LLM explanation string
    forecasting_window:int

def build_graph():
    builder = StateGraph(state_schema=StateSchema)

    builder.add_node("preprocess", preprocess_node)
    builder.add_node("forecast_baseline", forecast_baseline_node)
    builder.add_node("forecast_llm", forecast_llm_node)
    builder.add_node("evaluate", evaluate_node)
    builder.add_node("explain", explain_node)

    builder.set_entry_point("preprocess")
    builder.add_edge("preprocess", "forecast_baseline")
    builder.add_edge("forecast_baseline", "forecast_llm")
    builder.add_edge("forecast_llm", "evaluate")
    builder.add_edge("evaluate", "explain")

    builder.set_finish_point("explain")

    return builder.compile()