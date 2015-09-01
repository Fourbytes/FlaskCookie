from flask import Flask
app = Flask(__name__)


from . import controllers
from . import models


@app.errorhandler(404)
def handle_error_404(error):
	return render_template("errors/404.html"), 404