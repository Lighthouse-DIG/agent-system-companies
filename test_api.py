from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_fundamental import KeyValueRecursiveFlatten
from dotenv import load_dotenv
from datetime import datetime
import os
import pandas as pd

if __name__ == "__main__":
    # Cargar las variables del archivo .env
    load_dotenv()
    formatter_ = KeyValueRecursiveFlatten()
    # Obtener la API Key desde las variables de entorno
    apikey = os.getenv("ALPHAVANTAGE_API_KEY")
    data_request = FundamentalData(apikey=apikey)
    #data = data_request.get_balance_sheet(symbol="GOOGL")
    with open("mock/cash_flow.json") as f:
        import json
        data = json.load(f)

    def filter_annual_reports(data, start_date=None, end_date=None):
        start_date = start_date if start_date is not None else "1900-01-01"
        end_date = end_date if end_date is not None else (datetime.now() + pd.Timedelta(days=365)).strftime('%Y-%m-%d')
        data_df = pd.DataFrame(data["annualReports"])
        data_df["fiscalDateEnding"] = pd.to_datetime(data_df["fiscalDateEnding"])
        data_df = data_df.set_index("fiscalDateEnding").sort_index()
        data_df = data_df.loc[start_date:end_date]
        data["fiscalDateEnding"] = (
            data_df.rename(lambda x: x.strftime('%Y-%m-%d'))
                   .reset_index()
                   .to_dict(orient="records")
        )
        return data

