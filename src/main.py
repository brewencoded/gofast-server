from sanic import Sanic
from sanic.response import json, html
from sanic_cors import CORS, cross_origin
from json import load
from pymongo import MongoClient
from bson.json_util import dumps
import os

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
    cursor = db.inventory.find()
    results = map(lambda item: item, cursor)
    return json({ 'results': dumps(results)})


app.run(host="0.0.0.0", port=5000, debug=True)
