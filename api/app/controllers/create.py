import os, json
from flask import Blueprint, request, jsonify, redirect, url_for
from app.settings.database import db
from werkzeug.utils import secure_filename
from datetime import datetime

create = Blueprint('create', __name__, url_prefix='/api')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@create.route("/create", methods=['POST'])
def createProduct():
    if request.files and request.form:
        files = request.files.getlist('file')

        for file in files:
            data = {}
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
            data['fileName'] = file.filename

            result = db.product.insert_one(data)

            if file and allowedFile(file.filename):
                newFileName = str(result.inserted_id) + '.png'
                fileName = secure_filename(newFileName)
                file.save(os.path.join(UPLOAD_FOLDER, fileName))

                response = {
                    "success": True,
                    "message": "le fichier a été stocker dans le serveur"
                }
            else:
                db.product.delete_one({'_id': result.inserted_id})

                response = {
                    "success": False,
                    "message": "le fichier doit etre en format png, jpg ou jpeg"
                }
    else:
        response = {
                "success": False,
                "message": "Tout les attributs n'ont pas été envoyer"
         }
    
    return jsonify(response)
