import copy
import json

from flask import jsonify, request

from app.v1.proc_content import SpamModel
from . import api_v1

spm = SpamModel()


@api_v1.route('/v1')
@api_v1.route('/')
def default_get():
    resp = {
        'Info': 'Spam prediction API. Check if a message is spam or ham.',
        'Version': 'v1'
    }
    return jsonify(resp)


@api_v1.route('/v1/spam-ham', methods=['GET', 'POST'])
def spam_ham():
    if request.method == 'GET':
        resp = {
            "Instructions": "Post a document to evaluate using the format {'text': 'my message'}.",
            "Supported languages": "EN"
        }
    elif request.method == 'POST':
        req_data = json.loads(request.data)
        sp_model = copy.deepcopy(spm)
        sp_model.set_text(req_data.get('text'))
        resp = sp_model.predict()
    return jsonify(resp)



