from flask import Flask, flash, redirect, render_template, g, request, jsonify, url_for
import requests
import json


def get_pets():
    return json.loads(requests.get('http://54.210.155.165:3000/pets/main').content)
    