from prophet import Prophet
from datetime import datetime, timedelta
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta
from langchain.tools import tool
import quandl
import pandas as pd
import pickle

with open('./model/cashflow_prediction.pkl', 'rb') as f:
            # Load the object from the file
            MODEL= pickle.load(f)

class CashFlowPrediction:
    def __init__(self):
        pass
    @tool("predict cashflow")
    def forecast_cashflow(forecast_periods):
        """Generate future dates for forecasting."""
        model = MODEL
        current_date = datetime.today().date()
        future_dates = [current_date + timedelta(days=i) for i in range(1, int(forecast_periods)+1)]
        print(future_dates)
        # Convert future dates to a DataFrame
        future_df = pd.DataFrame({'ds': future_dates})

        # Make predictions for the future dates.
        forecast = model.predict(future_df)

        return forecast
    
    def load_model(self):
        with open('cashflow_prediction.pkl', 'rb') as f:
            # Load the object from the file
            return pickle.load(f)
