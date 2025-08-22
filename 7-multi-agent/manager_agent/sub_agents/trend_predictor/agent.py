import pandas as pd
from google.adk.agents import Agent 
from google.adk.tools import FunctionTool

def calculate_technical_indicators(historical_data: list) -> dict:
    """
    Input: historical_data = [{'Date': ..., 'Open': ..., 'High': ..., 'Low': ..., 'Close': ..., 'Volume': ...}, ...]
    Returns: dictionary of calculated indicators
    """
    df = pd.DataFrame(historical_data)
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    df['RSI_14'] = compute_rsi(df['Close'], 14)
    df['MACD'] = df['Close'].ewm(span=12, adjust=False).mean() - df['Close'].ewm(span=26, adjust=False).mean()
    return df[['Date', 'SMA_20', 'EMA_20', 'RSI_14', 'MACD']].to_dict(orient='records')

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

instruction_text="""
You are the Trend Predictor Agent, responsible for forecasting potential stock price and market movements.

Your tasks include:
- Identifying short-term and long-term market trends.
- Detecting momentum signals and reversals.
- Analyzing patterns in historical stock price movements.
- Highlighting potential breakout or breakdown points.

Guidelines:
- Base predictions on data-driven signals, not subjective opinions.
- Clearly distinguish between short-term and long-term outlooks.
- When uncertainty is high, indicate confidence levels or multiple possible scenarios.
- Present trend forecasts in a clear and structured way (e.g., tables, bullet points, probability ranges).
"""

trend_predictor = Agent(
    name="trend_predictor",
    model="gemini-2.0-flash",
    description="The Trend Predictor Agent forecasts short- and long-term stock market trends using historical data, patterns, and predictive signals.",
    instruction=instruction_text,
    tools=[
        FunctionTool(calculate_technical_indicators)
        ]  
        
)
