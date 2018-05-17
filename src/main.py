from sanic import Sanic
from sanic.response import json, html
from sanic_cors import CORS, cross_origin
from json import load
from pymongo import MongoClient
from bson.json_util import dumps
import os
import re

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.stock

app = Sanic(__name__)
CORS(app)

# servin dem assets
app.static('/public', './public')


# SPA route
@app.route('/')
async def index(request):
    index_page = open(os.getcwd() + '/public/index.html')
    return html(index_page.read())


@app.route('/api/search', methods=['GET'])
async def get_all(request):
    query = request.raw_args.get('query', None)
    # TODO: figure out how to set up full-text search in dockerfile
    # that is significantly more powerful and performant
    # This would also fix the issue with not being abe to query
    # aginst numeric field e.g. ID
    cursor = None
    if query is None or query == '':
        cursor = db.inventory.find()
    else:
        regex = re.compile('.*' + re.escape(query) + '.*', re.IGNORECASE)
        cursor = db.inventory.find({
            '$or': [
                {"Description": {'$regex' : regex}},
                {"lastSold": {'$regex' : regex}},
                {"ShelfLife": {'$regex' : regex}},
                {"Department": {'$regex' : regex}},
                {"Price": {'$regex' : regex}},
                {"Unit": {'$regex' : regex}},
                {"xFor": {'$regex' : regex}},
                {"Cost": {'$regex' : regex}}
            ]
        })
    results = map(lambda item: item, cursor)
    return json({ 'results': dumps(results)})


app.run(host="0.0.0.0", port=5000, debug=True)
