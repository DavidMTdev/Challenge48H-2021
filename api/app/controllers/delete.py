import os, json
from flask import Blueprint, request, jsonify, redirect, url_for
from app.settings.database import db
from werkzeug.utils import secure_filename
from datetime import datetime
from bson.objectid import ObjectId

delete = Blueprint('delete', __name__, url_prefix='/api')

@delete.route("/delete/<id>", methods=['POST'])
def deleteProduct(id):
    result = db.product.find_one({'_id': ObjectId(id)})
    if result:
        db.product.delete_one({'_id': ObjectId(id)})
        
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