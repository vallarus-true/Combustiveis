import json
import requests
from datetime import datetime

def executar_raspagem():
    dados = {
        "ultima_atualizacao": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "postos": [
            {"nome": "Posto 68 (BR 116)", "cidade": "Juquitiba", "distancia_km": 5, "gasolina": 6.79, "etanol": 4.70},
            {"nome": "Posto Shell (Centro)", "cidade": "Juquitiba", "distancia_km": 0, "gasolina": 6.85, "etanol": 4.90},
            {"nome": "Posto BR Petrobras (Régis)", "cidade": "São Lourenço da Serra", "distancia_km": 15, "gasolina": 6.72, "etanol": 4.65},
            {"nome": "Posto Ipiranga (Acesso Rodoanel)", "cidade": "Embu das Artes", "distancia_km": 32, "gasolina": 6.65, "etanol": 4.50},
            {"nome": "Posto Graal (Saída Raposo)", "cidade": "Cotia / Rodoanel", "distancia_km": 42, "gasolina": 6.59, "etanol": 4.45},
            {"nome": "Shell Select (Marginal / Brooklin)", "cidade": "São Paulo (Brooklin - R. Palmares)", "distancia_km": 58, "gasolina": 6.89, "etanol": 4.99},
            {"nome": "Ipiranga Rod. Pinheiros (Vila Madalena)", "cidade": "São Paulo (Vila Madalena - R. Paracuê)", "distancia_km": 64, "gasolina": 6.95, "etanol": 5.10},
            {"nome": "Posto BR (Litoral)", "cidade": "Itanhaém", "distancia_km": 85, "gasolina": 6.89, "etanol": 4.95}
        ]
    }

    try:
        with open('precos_juquitiba.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Matriz definitiva de postos gravada com sucesso.")
    except Exception as erro:
        print(f"Erro crítico: {erro}")
        exit(1)

if __name__ == "__main__":
    executar_raspagem()
