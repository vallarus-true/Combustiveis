import json
import requests
from datetime import datetime

def executar_raspagem():
    # Estrutura base de dados
    dados = {
        "ultima_atualizacao": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "postos": []
    }

    try:
        # Falsificação de assinatura para imitar um utilizador no Google Chrome
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        # ALVO: Aqui entra o URL do endpoint ou site de combustíveis.
        # url = 'https://site-fonte.com/precos/juquitiba'
        # resposta = requests.get(url, headers=headers, timeout=10)
        # resposta.raise_for_status()

        # [Lógica de extração do HTML (BeautifulSoup) entraria aqui]

        # Simulação temporária de dados injetados para testar o painel React
        dados["postos"] = [
            {"nome": "Posto 68 (BR 116)", "gasolina": 6.79, "etanol": 4.70},
            {"nome": "Posto Shell (Centro)", "gasolina": 6.85, "etanol": 4.90},
            {"nome": "Posto BR Petrobras", "gasolina": 6.75, "etanol": 4.80}
        ]

        # Geração do ficheiro de saída
        with open('precos_juquitiba.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
            
        print("Raspagem concluída. Ficheiro precos_juquitiba.json gerado.")

    except Exception as erro:
        print(f"Falha catastrófica durante a raspagem: {erro}")
        # Forçar falha no GitHub Actions para alertar o utilizador
        exit(1)

if __name__ == "__main__":
    executar_raspagem()
