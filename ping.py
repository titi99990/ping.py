import time
import requests

URL = "https://ton-projet.repl.co"  # Remplace par l'URL de ton Replit

def ping():
    while True:
        try:
            r = requests.get(URL)
            print(f"Ping {URL} - Status: {r.status_code}")
        except Exception as e:
            print(f"Erreur lors du ping: {e}")
        time.sleep(150)  # 150 secondes = 2 minutes 30
        

if __name__ == "__main__":
    ping()
