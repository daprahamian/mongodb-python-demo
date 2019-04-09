# Documentation here: https://api.mongodb.com/python/current/
from pymongo import MongoClient, WriteConcern
import datetime

# The db name you want to use
DB_NAME = 'test'
# The collection name you want to use
DATA_COLL_NAME = 'data'
# Analytics collection name
ANALYTICS_COLL_NAME = 'analytics'
# Reviews Collection Name
REVIEWS_COLL_NAME = 'reviews'

class MongoDBDao:
  def __init__(self, url):
    self._client = MongoClient(url)
    self._db = self._client[DB_NAME]
    self._data_collection = self._db[DATA_COLL_NAME]
    self._reviews_collection = self._db[REVIEWS_COLL_NAME]
    self._analytics_collection = self._db.get_collection(
      ANALYTICS_COLL_NAME, 
      write_concern = WriteConcern(w=0)
    )
  
  def get_data(self):
    return self._data_collection.find()
  
  def get_reviews(self):
    return self._reviews_collection.find()

  def save_reviews(self, username, content):
    self._reviews_collection.insert_one({
      'username': username,
      'content': content,
      'date': datetime.datetime.utcnow()
    })
  
  def get_analytics(self):
    return self._analytics_collection.find()

  def save_analytics(self, request, timestamp, response_code):
    duration = datetime.datetime.utcnow() - timestamp

    try:
      self._analytics_collection.insert_one({
        'timestamp': str(timestamp),
        'clientAddress': request.remote_addr,
        'path': request.path,
        'method': request.method,
        'duration': str(duration),
        'responseCode': response_code
      })
    except Exception:
      pass