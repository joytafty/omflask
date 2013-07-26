import flask, flask.views
import os
import utils

class Physical(flask.views.MethodView):
	@utils.login_required
	def get(self, page="physical"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class Embedgform(flask.views.MethodView):
	@utils.login_required
	def get(self, page="embedgform"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)
