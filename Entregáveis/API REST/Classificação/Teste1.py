#OBS: PARA O CÓDIGO RODAR O PROMPT TEM QUE ESTAR EM EXECUÇÃO

import requests

url = 'http://127.0.0.1:5000/prever'

dict_json = {
    'Fase': 3.1,
    'Período de tempo': 33,
    'Valor': 25.8,
    'CI baixo': 21.4,
    'CI alto': 30.5
}

response = requests.get(url, params=dict_json)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro: {response.status_code}")
