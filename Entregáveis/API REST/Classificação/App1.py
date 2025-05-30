from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)


with open("C:\\Users\\Windows 10\\Desktop\\GS AI&ChatBot\\Entregáveis\\meu_modelo_serializado_classificacao.pickle", 'rb') as f:
    modelo1 = pickle.load(f)


@app.route('/prever', methods=['GET'])
def prever():
    
    parametro1 = float(request.args.get('Fase'))
    parametro2 = float(request.args.get('Período de tempo')) 
    parametro3 = float(request.args.get('Valor'))
    parametro4 = float(request.args.get('CI baixo'))
    parametro5 = float(request.args.get('CI alto'))


    entrada = np.array([[parametro1, parametro2, parametro3, parametro4, parametro5]])
    resultado = modelo1.predict(entrada)

    return jsonify({'Diagnósticos': resultado.tolist()})

if __name__ == '__main__':
    print("Servidor Flask em execução")
    app.run(debug=True)