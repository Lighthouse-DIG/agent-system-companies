from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
apikey = os.getenv("ALPHAVANTAGE_API_KEY")
data = FundamentalData(apikey=apikey).get_overview(symbol="GOOG")
print(data)
