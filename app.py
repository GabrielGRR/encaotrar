import sqlite3 as sql
from flask import Flask, flash, redirect, render_template, g, request, jsonify, url_for
import requests
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from api.api import get_pets

# Configure application
app = Flask(__name__)

text_obj = open("api_key.txt","r",encoding="utf-8")
api_key = text_obj.read()

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = api_key

# Initialize the extension
GoogleMaps(app)

#Inicialização do index
@app.route('/', methods=["POST","GET"], defaults={'location': '-19.9288902,-43.9379158'})
@app.route('/<location>', methods=["POST","GET"])
def index(location='-19.9288902,-43.9379158'):
    location = request.args.get('location')
    if(location == None):
        location = '-19.9288902,-43.9379158'
    pets = get_pets()
    #pets = [{'_id': '673e51dc663324626c5d736d', 'name': 'dcxcvz', 'local': 'fdsfwewetfw', 'dono': 'fdsfsdf', 'lat': {'$numberDecimal': '130.234'}, 'lng': {'$numberDecimal': '-140320'}, 'dataDes': '1980-08-04T10:55:25.636Z', 'image': '438c76c32e76a8a720d49c7de1137785f3ec5f2f09b45f120faad5d8087c441e', 'createdAt': '2024-11-20T21:17:16.210Z', 'updatedAt': '2024-11-20T21:17:16.210Z', '__v': 0, 'imageUrl': 'https://a3mainbucket.s3.us-east-1.amazonaws.com/438c76c32e76a8a720d49c7de1137785f3ec5f2f09b45f120faad5d8087c441e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIASYG2FTVHA7WVF5MV%2F20241120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241120T212106Z&X-Amz-Expires=3600&X-Amz-Signature=df1ceab49a4f57789069c0b91565af530cbf7ce7dfc4a62da5efc75b8e63c746&X-Amz-SignedHeaders=host&x-id=GetObject'}]
    print(location)
    lista_provisoria_animais = ["Caiçara - 7 horas atrás", "Barro Preto - 15 horas atrás", "Santa Mônica - 10/10/24 19:35", "Funcionários - 09/10/24 08:23", "Coração Eucarístico - 09/10/24 07:49"]
    return render_template('index.html', lista_animais = pets, api_key=api_key, location=location)

if __name__ == '__main__':
    app.run(debug=True)
