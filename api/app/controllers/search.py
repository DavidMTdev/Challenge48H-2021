import os
from flask import Blueprint, request, jsonify, redirect, url_for, send_file, send_from_directory
from app.settings.database import db
from bson.objectid import ObjectId

search = Blueprint('search', __name__, url_prefix='/api')

UPLOAD_FOLDER = 'uploads'

@search.route("/search", methods=['POST'])
def getSearch():
    data = {}

    for r in request.form:
        if request.form[r]:
            data[r] = request.form[r]

    results = db.product.find(data)

    response = {
            "success": True,
            "message": "le fichier a été stocker dans le serveur",
            "results": []
    }

    for result in results:
        r = {}
        r['name'] = result['name']
        r['id'] = str(result['_id'])
        r['image'] = {}
        r['image']['url'] = request.url_root + 'api/search/image/' + str(result['_id']) + '/' + result['fileName']
        r['image']['name'] = result['fileName']

        response['results'].append(r)
    
    return jsonify(response)

@search.route("/search/<id>", methods=['GET'])
def getSearchById(id):
    
    result = db.product.find_one({'_id': ObjectId(id)})

    if result:
        response = {
            "success": True,
            "message": "le fichier a été stocker dans le serveur",
            "result": {
                'id': str(result['_id']),
                'name': result['name'],
                'type': result['type'],
                'picture_product': result['picture_product'],
                'picture_human': result['picture_human'],
                'picture_institutional': result['picture_institutional'],
                'format': result['format'],
                'credits': result['credits'],
                'limited_utilisation_right': result['limited_utilisation_right'],
                'copyright': result['copyright'],
                'deadline_utilisation_right': result['deadline_utilisation_right'],
                'tags': result['tags'],
                'fileName': result['fileName']
            }
        }
    else:
        response = {
            "success": False,
            "message": "le fichier a été stocker dans le serveur",
        }

    return jsonify(response)

@search.route('/search/image/<id>/<file>', methods=['GET'])
def getImage(id, file):
    filename = id + '.png'
    return send_file(os.path.join(UPLOAD_FOLDER, filename))
