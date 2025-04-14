from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_fundamental import KeyValueRecursiveFlatten
from dotenv import load_dotenv
import os
import pandas as pd

#if __name__ == "__main__":
#    # Cargar las variables del archivo .env
#    load_dotenv()
#    formatter_ = KeyValueRecursiveFlatten()
#    # Obtener la API Key desde las variables de entorno
#    apikey = os.getenv("ALPHAVANTAGE_API_KEY")
#    data_request = FundamentalData(apikey=apikey)
#    data = data_request.get_balance_sheet(symbol="GOOGL")
#    data = pd.DataFrame(data["annualReports"])
#    data["fiscalDateEnding"] = pd.to_datetime(data["fiscalDateEnding"])
#    data = data.set_index("fiscalDateEnding").sort_index()
#    data = data.loc["2023-12-31":"2024-12-31"]
#    print(data)
