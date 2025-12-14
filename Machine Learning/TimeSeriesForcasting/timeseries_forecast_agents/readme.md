# ⏱️ Time Series Forecasting with Prophet and LLM Agents (LangGraph + Ollama)

This project demonstrates how to build a multi-agent time series forecasting system using [LangGraph](https://github.com/langchain-ai/langgraph), a graph-based orchestration framework, and local LLMs via [Ollama](https://ollama.com). The system compares traditional forecasting (via Prophet) with LLM-based predictions, evaluates performance, and explains the results using an LLM.

📈 The forecasting task is performed on retail sales data, where the goal is to predict the next 7 days of sales based on historical trends. Each step in the pipeline — preprocessing, forecasting, evaluating, and explanation — is modularized into LangGraph nodes, making the system easily inspectable and extensible.

## 🔧 Features

- **Graph-based pipeline** using LangGraph
- **Baseline forecast** with Facebook Prophet
- **LLM forecast** using LLaMA 3.2 (via Ollama)
- **Evaluation metrics**: RMSE, MAE, SMAPE
- **LLM explanation** of which model performed better and why
- **Modular agents**: each stage is a separate function for extensibility


## 📦 Project Structure
```
ts_forecast_langgraph/
├── main.py # Entry point
├── graph.py # LangGraph pipeline definition
├── data.csv # Retail sales time series (Kaggle-style)
├── requirements.txt
└── nodes/ # Node logic
    ├── preprocess.py # Load, smooth, and slice data
    ├── forecast_baseline.py # Forecast with Prophet
    ├── forecast_llm.py # Forecast with LLM 
    ├── evaluate.py # RMSE, MAE, SMAPE computation
    └── explain.py # LLM-based evaluation summary
```

## ⚙️ Setup Instructions

### 1. Clone the repo and create a virtual environment

```
git clone https://github.com/vikrambhat2/timeseries_forecast_agents.git
cd ts_forecast_langgraph
python3 -m venv ts_venv
source ts_venv/bin/activate
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Start Ollama with a LLaMA model
```
ollama run llama3.3
```
⚠️ Make sure llama3 is downloaded and running locally before executing forecasts.

4. Run the forecast pipeline
```
python main.py
```

## Use Cases
- Benchmarking traditional vs LLM-based forecasting
- Teaching hybrid AI systems with symbolic and neural components
- Creating explainable time series predictions
- Prototype for plugging into LangChain MCP toolchains


## Future Enhancements
- Add Hugging Face fine-tuned time series models
- Visualize forecast comparison with matplotlib/plotly
- Serve as an MCP-compatible server for external LLM clients
- Integrate with Streamlit for interactive UI