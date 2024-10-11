import sqlite3 as sql
from flask import Flask, flash, redirect, render_template, g, request, jsonify, url_for 
import requests

# https://github.com/heremaps/maps-api-for-javascript-examples
# here maps api google search

### https://github.com/flask-extensions/Flask-GoogleMaps


# Configure application
app = Flask(__name__)



#Inicialização do index
@app.route('/', methods=["POST","GET"])
def index():
    lista_provisoria_animais = ["Caiçara - 7 horas atrás", "Barro Preto - 15 horas atrás", "Santa Mônica - 10/10/24 19:35", "Funcionários - 09/10/24 08:23", "Coração Eucarístico - 09/10/24 07:49"]
    return render_template('index.html', lista_animais = lista_provisoria_animais)

if __name__ == '__main__':
    app.run(debug=True)
