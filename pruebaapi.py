from acquisition.acquisition.alphavantage.fundamental_data import FundamentalData
from dotenv import load_dotenv
# Cargar las variables del archivo .env
load_dotenv()

# Obtener la API Key desde las variables de entorno
apikey = os.getenv("ALPHAVANTAGE_API_KEY")
data = FundamentalData(apikey=apikey).get_overview(symbol="GOOGL")
print(data)
