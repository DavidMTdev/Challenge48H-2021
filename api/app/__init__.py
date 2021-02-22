from flask import Flask
from flask_cors import CORS

from app.settings.config import Config
# Import routes
from app.controllers.search import search
from app.controllers.create import create

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

# route
app.register_blueprint(search)
app.register_blueprint(create)
