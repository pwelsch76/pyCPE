"""
This script runs the pyCPE application using a development server.
"""

from os import environ
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Multi(Resource):
       
       def post(self):
            some_json = request.get_json()
            return {"Enviado": some_json}, 201

       def get(self, num):
            return {'result': num*10}

api.add_resource(Multi, '/multi/<int:num>')
        
if __name__ == '__main__':
     app.run(debug=False)