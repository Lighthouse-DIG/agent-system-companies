from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from format_tool.format_fundamental import KeyValueRecursiveFlatten
from dotenv import load_dotenv
import os
# Cargar las variables del archivo .env
load_dotenv()
formatter_ = KeyValueRecursiveFlatten()
# Obtener la API Key desde las variables de entorno
apikey = os.getenv("ALPHAVANTAGE_API_KEY")
data_request = FundamentalData(apikey=apikey)
data = data_request.get_overview(symbol="GOOGL")
print(data)
print(formatter_(data))
data = data_request.get_balance_sheet(symbol="GOOGL")
print(formatter_(data))
