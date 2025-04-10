from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from dotenv import load_dotenv
import os
# Cargar las variables del archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
apikey = os.getenv("ALPHAVANTAGE_API_KEY")
data_request = FundamentalData(apikey=apikey)
data = data_request.get_overview(symbol="GOOGL")
print(data)
data = data_request.get_balance_sheet(symbol="GOOGL")
print(data)