import redis
from flask import Flask
from flask import request
from rq import Queue
from base_api import insert_into_mongo

app = Flask(__name__)
q = Queue(connection=redis.Redis(host='redis', port=6379, db=0))

@app.route('/')
def event():
    data = {'request_type': request.method}
    job = q.enqueue(insert_into_mongo, data)
    print(job.result)     
    return str(job.__dict__)

if __name__ == '__main__':
    app.run(debug='true', host='0.0.0.0', port='8888')
