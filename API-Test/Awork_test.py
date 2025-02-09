import requests
import os
from dotenv import load_dotenv

# Lade Umgebungsvariablen für Awork-API
load_dotenv()
awork_api_key = os.getenv("AWORK_API_KEY")


# URL für Awork-Tasks
url = "https://api.awork.com/api/v1/me/taskviews"

# Header für die Authentifizierung
headers = {
    "Authorization": f"Bearer {awork_api_key}"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    print("Status Code:", response.status_code)
    print("Response:", response.text)
except requests.exceptions.Timeout:
    print("❌ Timeout! Awork antwortet nicht.")
except requests.exceptions.ConnectionError:
    print("❌ Verbindungsfehler! Ist die URL korrekt?")
except Exception as e:
    print("❌ Ein anderer Fehler:", str(e))
