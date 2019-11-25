from flask_restful import Resource
from urllib.request import urlopen
import json

class FreeFood(Resource):
    def get(self):
        response = urlopen("http://uiucfreefood.com/appJson/")
        return json.load(response)
