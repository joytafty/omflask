import flask, flask.views
import os

class d3Charts(flask.views.MethodView):
	def get(self, page="d3charts"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)
