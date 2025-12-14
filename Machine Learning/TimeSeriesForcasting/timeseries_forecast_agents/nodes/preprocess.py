import pandas as pd
from typing import Dict
from io import StringIO

def preprocess_node(state):
    df = pd.read_json(StringIO(state.input_data))
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index("date").asfreq("D")
    df['sales'] = df['sales'].ffill()
    df['rolling_mean_7'] = df['sales'].rolling(7).mean()
    preprocessed_df = df.dropna().tail(30)
    return {
        **state.model_dump(),
        "preprocessed_df": preprocessed_df.reset_index().to_json(orient="records", date_format="iso")
    }