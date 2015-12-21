from flask import Flask, render_template
app = Flask(__name__)

# Load the config
env_config = os.environ.get('APP_CONFIG') or 'DevelopmentConfig'
print(' * Loading config: ' + 'config.app_config.{}'.format(env_config))
app.config.from_object('config.app_config.{}'.format(env_config))

# Fix for behind reverse proxy
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

# Setup the database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Import our things
import application.controllers
import application.models

# Create tables n' things.
db.create_all()


# Register basic error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
