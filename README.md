# mongodb-python-demo

## Dependencies

+ [python](https://www.python.org/) >=v3
+ [pip](https://pypi.org/project/pip/)
+ [pymongo](https://api.mongodb.com/python/current/) >=v3.7.2 (`python -m pip install pymongo`)
+ [bottle](https://bottlepy.org/docs/dev/) >=v0.12.16 (`python -m pip install bottle`)

## Setup

In [`server.py`](server.py), change `MONGODB_URL` to point to your mongodb cluster

## Running the server

```python
python server.py
```

This should start the server on `localhost:8080`
