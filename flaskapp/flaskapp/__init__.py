from flask import Flask, render_template
app = Flask(__name__)

# Load the config
import json
with open('config.json') as f:
	app.config.update(json.load(f))


# Setup the database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
db.create_all()


# Import our things
from . import controllers
from . import models


# Register basic error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500