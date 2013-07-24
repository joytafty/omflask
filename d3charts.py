import flask, flask.views
import os
import utils

class d3Charts(flask.views.MethodView):
	@utils.login_required
	def get(self, page="d3charts"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class dcCharts(flask.views.MethodView):
	def get(self, page="dcindex"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)