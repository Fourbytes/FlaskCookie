from flask import render_template, request
from flask.ext.classy import FlaskView

class HelloWorldController(FlaskView):
	def index(self):
		return render_template('index.html', ip=request.remote_addr)