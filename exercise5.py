from flask import Flask, request
from json import dumps, loads
from exercise4 import find_object, update_object 

app = Flask(__name__)

@app.route('/<oid>', methods=['GET'])
def findobject(oid):
  obj = find_object(oid)
  return dumps(obj)

@app.route('/<oid>', methods=['POST', 'PUT'])
def updateObject(oid):
  obj = loads(request.get_data())
  obj['name'] = oid
  update_object(obj)
  print 'I got a post request!'
  return ""

if __name__ == '__main__':
   app.testing = True
   with app.test_client() as c:
     post_resp = c.post('/name', data=dumps({'whatever': 'youwant'}))
     get_resp = c.get('/name')
     print 'status: %s' % post_resp.status
     print 'response: %s' % get_resp.get_data()
