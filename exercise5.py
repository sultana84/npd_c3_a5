from flask import Flask
from json import dumps, loads
from exercise4 import find_object, update_object 

app = Flask(__name__)

client = MongoClient()
my_collection = client.my_database.my_collection

@app.route('/<oid>', methods=['GET'])
def findobject(oid):
  obj = find_object(oid)
  return dumps(obj)

@app.route('/<oid>', methods=['POST', 'PUT'])
def updateObject(oid):
  obj = loads(request.get_data(),)
  update_object = obj['I got a post request!']
  print 'I got a post request!'
  return ""

if __name__ == '__main__':
   with app.test_client() as c:
     get_resp = c.get('/blah')
     print 'get status: %s' % get_resp.status
     print 'get response: %' % get_resp.get_data()
     post_resp = c.post('/blah')

