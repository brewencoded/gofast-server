from sanic import Sanic
from sanic.response import json, html
from sanic_cors import CORS, cross_origin
from json import load

import os

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
    with open(os.getcwd() + '/test/mocks/inventory.json') as json_data:
        mock_inventory = load(json_data)
        return json({ 'results': mock_inventory})


app.run(host="0.0.0.0", port=5000, debug=True)
