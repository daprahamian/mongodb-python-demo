# Documentation here: https://api.mongodb.com/python/current/
from pymongo import MongoClient, WriteConcern
from dao import MongoDBDao

# Documentation here: https://bottlepy.org
from bottle import Bottle, run, template, request, response, static_file

import datetime

# Config Options

# Replace the below with your Atlas URL
MONGODB_URL = 'mongodb://localhost:27017/'
# The url you want to run this server on
APP_HOST = 'localhost'
# The Port you want to run this server on
APP_PORT = 8080
# Set to false to disable debug mode
DEBUG = True

# Your application, which runs an http server
app = Bottle()

# Object to communicate with the database
dao = MongoDBDao(MONGODB_URL)

# Change this to the fields you want to display from your data set
data_columns = ['_id']
analytics_columns = [ 'timestamp', 'clientAddress', 'path', 'responseCode' ]
reviews_columns = ['username', 'content']
reviews_labels = ['User', 'Review']

def err_msg(err):
  return 'Error: {}'.format(err) if DEBUG else 'An Error Occurred'

@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@app.get('/')
def homepage():
  return template('homepage', submitted=False)

@app.post('/')
def post_review():
  start = datetime.datetime.utcnow()
  responseCode = 200
  try:
    dao.save_reviews(request.forms.get('username'), request.forms.get('content'))
    return template('homepage', submitted=True)
  except Exception as e:
    responseCode = 500
    response.status = responseCode
    return err_msg(e)
  finally:
    # Try to log analytics. We do not care if this fails
    dao.save_analytics(request, start, responseCode)

@app.get('/data')
def get_data():
  start = datetime.datetime.utcnow()
  responseCode = 200
  try:
    docs = dao.get_data()
    return template('data', docs=docs, columns=data_columns, title='Analytics')
  except Exception as e:
    responseCode = 500
    response.status = responseCode
    return err_msg(e)
  finally:
    # Try to log analytics. We do not care if this fails
    dao.save_analytics(request, start, responseCode)

@app.get('/reviews')
def get_reviews():
  start = datetime.datetime.utcnow()
  responseCode = 200
  try:
    docs = dao.get_reviews()
    return template('reviews', docs=docs)
  except Exception as e:
    responseCode = 500
    response.status = responseCode
    return err_msg(e)
  finally:
    # Try to log analytics. We do not care if this fails
    dao.save_analytics(request, start, responseCode)

@app.get('/analytics')
def get_analytics():
  start = datetime.datetime.utcnow()
  responseCode = 200
  try:
    docs = dao.get_analytics()
    return template('analytics', docs=docs, columns=analytics_columns, title='Analytics')
  except Exception as e:
    responseCode = 500
    response.status = responseCode
    return err_msg(e)
  finally:
    # Try to log analytics. We do not care if this fails
    dao.save_analytics(request, start, responseCode)

run(app, host=APP_HOST, port=APP_PORT, reloader=DEBUG)
