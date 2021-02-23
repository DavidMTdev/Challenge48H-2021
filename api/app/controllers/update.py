import os, json
from flask import Blueprint, request, jsonify, redirect, url_for
from app.settings.database import db
from werkzeug.utils import secure_filename
from datetime import datetime
from bson.objectid import ObjectId


update = Blueprint('update', __name__, url_prefix='/api')

UPLOAD_FOLDER = 'app/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@update.route("/update/<id>", methods=['POST'])
def updateProduct(id):
    result = db.product.find_one({'_id': ObjectId(id)})
    data = {}
    if result:
        if request.form:
            data['name'] = request.form['name']
            data['type'] = request.form['type']
            data['picture_product'] = request.form['picture_product']
            data['picture_human'] = request.form['picture_human']
            data['picture_institutional'] = request.form['picture_institutional']
            data['format'] = request.form['format']
            data['credits'] = request.form['credits']
            data['limited_utilisation_right'] = request.form['limited_utilisation_right']
            data['copyright'] = request.form['copyright']
            data['deadline_utilisation_right'] = request.form['deadline_utilisation_right']
            data['tags'] = request.form['tags'].split(',')

        if request.files:
            file = request.files['file']

            if file and allowedFile(file.filename):
                newFileName = id + '.png'
                fileName = secure_filename(newFileName)
                file.save(os.path.join(UPLOAD_FOLDER, fileName))
                data['fileName'] = file.filename

        result = db.product.update_one({'_id': ObjectId(id)}, {'$set': data})

        response = {
            "success": True,
            "message": "Tout les attributs n'ont pas été envoyer"
        }

    else:
        response = {
            "success": False,
            "message": "Tout les attributs n'ont pas été envoyer"
        }
    
    return jsonify(response)
