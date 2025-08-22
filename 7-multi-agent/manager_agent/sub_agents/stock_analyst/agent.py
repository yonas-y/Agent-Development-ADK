import yfinance as yf
from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import FunctionTool

# -------- Tool Functions -------- #

def get_stock_price(ticker: str) -> dict:
    """
    Fetches the latest stock price for a given ticker symbol.
    """
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]
        return {
            "ticker": ticker.upper(),
            "price": round(price, 2),
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        return {"error": str(e)}


def get_historical_stock_data(ticker: str, period: str = "1mo", interval: str = "1d") -> dict:
    """
    Fetches historical stock data for a given ticker symbol.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)
        data = hist.reset_index().to_dict(orient="records")
        
        return {
            "ticker": ticker.upper(),
            "period": period,
            "interval": interval,
            "data_points": len(data),
            "historical_data": data
        }
    except Exception as e:
        return {"error": str(e)}

instruction_text="""
You are the Stock Analyst Agent, responsible for analyzing stock-related data.

Your tasks include:
- Performing fundamental analysis (e.g., revenue, P/E ratio, earnings reports, financial health).
- Conducting technical analysis (e.g., moving averages, support/resistance levels, trend indicators).
- Comparing multiple stocks to highlight relative strengths and weaknesses.
- Providing clear, data-driven insights that can support investment decisions.
- Use the tools, get_stock_price and get_historical_stock_data, to fetch relevant data for your analysis.

Guidelines:
- Be precise and use quantifiable metrics when possible.
- Explain technical indicators and their implications clearly.
- Avoid subjective opinions; base analysis on data, trends, and recognized financial methods.
- Present results in a structured, easy-to-read format (tables, bullet points, or summaries).
"""

stock_analyst_agent = Agent(
    name="stock_analyst",
    model="gemini-2.0-flash",
    description="The Stock Analyst Agent performs technical and fundamental analysis of stocks, " \
    "identifying patterns, key metrics, and investment opportunities.",
    instruction=instruction_text,
    tools=[
        FunctionTool(get_stock_price), 
        FunctionTool(get_historical_stock_data)
        ]
)
