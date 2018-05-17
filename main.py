from sanic import Sanic
from sanic.response import json, html
import os

app = Sanic(__name__)

# servin dem assets
app.static('/public', './public')


# SPA route
@app.route('/')
async def index(request):
    index_page = open(os.getcwd() + '/public/index.html')
    return html(index_page.read())


app.run(host="0.0.0.0", port=5000, debug=True)
