import flask, flask.views
import os

class Charts(flask.views.MethodView):
	def get(self, page="charts"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)
