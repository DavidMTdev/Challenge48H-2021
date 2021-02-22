from flask import Flask
from app.settings.config import Config
# Import routes
from app.controllers.search import search
from app.controllers.create import create

app = Flask(__name__)
app.config.from_object(Config)

# route
app.register_blueprint(search)
app.register_blueprint(create)
