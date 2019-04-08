# Documentation here: https://api.mongodb.com/python/current/
from pymongo import MongoClient, WriteConcern

# Documentation here: https://bottlepy.org
from bottle import Bottle, run, template, request, response

import datetime

# Config Options

# Replace the below with your Atlas URL
MONGODB_URL = 'mongodb://localhost:27017/'
# The url you want to run this server on
APP_HOST = 'localhost'
# The Port you want to run this server on
APP_PORT = 8080
# The db name you want to use
DB_NAME = 'test'
# The collection name you want to use
DATA_COLL_NAME = 'test'
# Analytics collection name
ANALYTICS_COLL_NAME = 'analytics'

# Your application, which runs an http server
app = Bottle()

# Your MongoClient, which speaks to the database
client = MongoClient(MONGODB_URL)

# The db you are using
db = client[DB_NAME]

# Collection objects
data_collection = db[DATA_COLL_NAME]
analytics_collection = db.get_collection(
  ANALYTICS_COLL_NAME, 
  write_concern = WriteConcern(w=0)
)

# Change this to the fields you want to display from your data set
data_columns = ['_id']
analytics_columns = [ 'timestamp', 'clientAddress', 'path', 'responseCode' ]

def send_analytics(_request, timestamp, response_code):
  duration = datetime.datetime.utcnow() - timestamp

  try:
    obj = {
      'timestamp': str(timestamp),
      'clientAddress': _request.remote_addr,
      'path': _request.path,
      'method': _request.method,
      'duration': str(duration),
      'responseCode': response_code
    }
    analytics_collection.insert_one(obj)
  except:
    pass

@app.route('/')
def hello():
  return 'Hello World'

@app.route('/data')
def get_data():
  start = datetime.datetime.utcnow()
  ret = None
  responseCode = 200
  try:
    docs = data_collection.find({})
    ret = template('table', docs=docs, columns=data_columns)
  except:
    responseCode = 500
    ret = 'There was some kind of error'
  
  # Try to log analytics. We do not care if this fails
  send_analytics(request, start, responseCode)
  
  response.status = responseCode
  return ret

@app.route('/analytics')
def get_analytics():
  start = datetime.datetime.utcnow()
  ret = None
  responseCode = 200
  try:
    docs = analytics_collection.find({})
    ret = template('table', docs=docs, columns=analytics_columns)
  except:
    responseCode = 500
    ret = 'There was some kind of error'
  
  # Try to log analytics. We do not care if this fails
  send_analytics(request, start, responseCode)
  
  response.status = responseCode
  return ret

run(app, host=APP_HOST, port=APP_PORT, reloader=False)
