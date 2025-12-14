import json
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2:1b")

def explain_node(state):
    prompt = f"""
Compare these forecasts:
Prophet: {json.dumps(state.baseline_forecast)}
LLM: {json.dumps(state.llm_forecast)}
Ground Truth: {json.dumps(state.ground_truth)}
Error Metrics from Prophet Forecast:{json.dumps(state.baseline_scores)}
Error Metrics from LLM Forecast:{json.dumps(state.llm_scores)}
Which model performed better? Explain key trends and differences in a few lines.
"""
    response = llm.invoke(prompt)
    return {**state.model_dump(), "explanation": response.content.strip()}