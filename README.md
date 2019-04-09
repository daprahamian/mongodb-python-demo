# mongodb-python-demo

## Installation

1. Install [python](https://www.python.org/)
2. Run the following command

```sh
python3 -m pip install -r requirements.txt
```

This will install the following:

+ [pymongo](https://api.mongodb.com/python/current/)
  + with tls support
  + with srv support
+ [bottle](https://bottlepy.org/docs/dev/)

## Setup

In [`server.py`](server.py), change `MONGODB_URL` to point to your mongodb cluster

## Running the server

```python
python server.py
```

This should start the server on `localhost:8080`
