import flask, flask.views
import os
import utils

class About(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template('about.html')

	@utils.login_required
	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('about'))