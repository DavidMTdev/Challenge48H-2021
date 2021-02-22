from flask import Blueprint, request, jsonify, redirect, url_for
from app.settings.database import db

search = Blueprint('movie', __name__, url_prefix='/api')

@search.route("/search")
def getMovie():
    return "frerger"
