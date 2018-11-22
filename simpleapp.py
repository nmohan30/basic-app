from flask import Flask
from redis import Redis
import sys
import optparse
import time

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


start = int(round(time.time()))

@app.route("/")
def hello_world():
    redis.incr('hits')
    return "Hello world! This page has been viewed %s time(s)." % redis.get('hits')
    

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
