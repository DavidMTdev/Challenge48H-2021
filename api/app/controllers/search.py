from flask import Blueprint, request, jsonify, redirect, url_for
from app.settings.database import db

search = Blueprint('search', __name__, url_prefix='/api')

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
        response['results'].append(r)

    
    return jsonify(response)
