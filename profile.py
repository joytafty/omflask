import flask, flask.views
import os
import utils

class Profile(flask.views.MethodView):
	@utils.login_required
	def get(self, page="user-profile"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)