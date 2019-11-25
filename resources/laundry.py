from flask_restful import Resource
from urllib.request import urlopen
import json

class Laundry(Resource):
    def get(self):
      request_url = "http://23.23.147.128/homes/mydata/urba7723"
      response = urlopen(request_url)
      return json.load(response)
