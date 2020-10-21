import os
from flask import Flask, jsonify, request
from math import sqrt


app = Flask(__name__)


@app.route('/')
def sequencia_fibo():
    lista_fibo = [0, 1]
    for i in range(1, 49):
        a = lista_fibo[i] + lista_fibo[i-1]
        lista_fibo.append(a)
    b = str(lista_fibo)
    return b


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
