from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse,request

import json


# Create app object(instance) from Flask library
app = Flask(__name__)


# Create api object using flask-app object
api = Api(app)

@app.route('/api/get_location/<string:location>', methods=['GET'])
def get_location(location):
   record = location
   with open('parking_lots.json', 'r') as f:
      data = f.read()
   records={}
   if not data:
      return {"Msg:":"Not Found!"}
   else:
      records = json.loads(data)
      return jsonify(records[record])


@app.route('/api/add_location', methods=['POST'])
def add_location():
   record = json.loads(request.data)
   with open('parking_lots.json', 'r') as f:
      data = f.read()
   records={}
   if not data:
      records = record["parkinglot"]
   else:
      records = json.loads(data)
      records.update(record["parkinglot"])
   f = open("parking_lots.json", "w")
   f.write(json.dumps(records, indent=4))
   f.close()
   return jsonify(record["parkinglot"])


@app.route('/api/update_location', methods=['PUT'])
def update_location():
   record = json.loads(request.data)
   with open('parking_lots.json', 'r') as f:
      data = f.read()
   records={}
   if not data:
      records = record["parkinglot"]
   else:
      records = json.loads(data)
      for key,val in record["parkinglot"].items():
         if key in records:
            records[key]=val
   f = open("parking_lots.json", "w")
   f.write(json.dumps(records, indent=4))
   f.close()
   return jsonify(record["parkinglot"])


@app.route('/api/delete_location/<string:location>', methods=['DELETE'])
def delete_location(location):
   record = location
   with open('parking_lots.json', 'r') as f:
      data = f.read()
   records={}
   if not data:
      return {"Msg:":"No data found!"}
   else:
      records = json.loads(data)
      if record in records:
         del records[record]
   f = open("parking_lots.json", "w")
   f.write(json.dumps(records, indent=4))
   f.close()
   return {"Msg:":"Deleted!"}


# Run the flask-app server
if __name__ == "__main__":
   app.run(debug=True)