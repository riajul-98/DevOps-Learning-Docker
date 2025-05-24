# Importing packages
import os
from flask import Flask
import redis

app = Flask(__name__)

# Setting environment variables
redis_host = os.getenv('REDIS_HOST', 'redisdb')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)

# Creating route route for simple application
@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'

# Creating count route using redis visit count
@app.route('/count')
def visit_count():
    count = r.incr('visits')
    return f'This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)