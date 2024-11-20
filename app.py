import sqlite3 as sql
from flask import Flask, flash, redirect, render_template, g, request, jsonify, url_for
import requests
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

# Configure application
app = Flask(__name__)

text_obj = open("api_key.txt","r",encoding="utf-8")
api_key = text_obj.read()

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = api_key

# Initialize the extension
GoogleMaps(app)

#Inicialização do index
@app.route('/', methods=["POST","GET"])
def index():

    
    lista_provisoria_animais = ["Caiçara - 7 horas atrás", "Barro Preto - 15 horas atrás", "Santa Mônica - 10/10/24 19:35", "Funcionários - 09/10/24 08:23", "Coração Eucarístico - 09/10/24 07:49"]
    return render_template('index.html', lista_animais = lista_provisoria_animais, api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)
