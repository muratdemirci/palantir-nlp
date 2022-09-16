from ast import Try
from asyncio.windows_events import NULL
from contextlib import nullcontext
from flask import Flask
import nlp
from flask import request
from flask import Response
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return {'success':True}

@app.route('/data', methods=["POST"])
def theWord():
    try:
        input_json = request.get_json(force=True)
        return {'score':nlp.score(input_json['text']),'success':True}
    except:
        print(sys.exc_info()[0])
        return Response({'score':'','success':False}, status=500, mimetype='application/json')