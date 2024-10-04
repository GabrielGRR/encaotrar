import sqlite3 as sql
from flask import Flask, flash, redirect, render_template, g, request, jsonify, url_for 

# https://github.com/heremaps/maps-api-for-javascript-examples
# here maps api google search

# Configure application
app = Flask(__name__)

#Inicialização do index
@app.route('/', methods=["POST","GET"])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
