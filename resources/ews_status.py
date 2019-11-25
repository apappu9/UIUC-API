from flask_restful import Resource
from urllib.request import urlopen
import re
import json

class EWSStatus(Resource):
    def get(self):
        response = urlopen("https://my.engr.illinois.edu/labtrack/util_data_json.asp")
        return json.load(response)
