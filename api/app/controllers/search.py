from flask import Blueprint, request, jsonify, redirect, url_for
from app.settings.database import db

search = Blueprint('search', __name__, url_prefix='/api')

@search.route("/search")
def getSearch():
    return "frerger"
