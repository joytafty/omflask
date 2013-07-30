import flask, flask.views
import os
import utils

class gform(flask.views.MethodView):
	@utils.login_required
	def get(self, page="gform"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class Qpreboarding(flask.views.MethodView):
	@utils.login_required
	def get(self, page="questionnaire-preboarding"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class Qonboarding(flask.views.MethodView):
	@utils.login_required
	def get(self, page="questionnaire-onboarding"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class Q24hfood(flask.views.MethodView):
	@utils.login_required
	def get(self, page="questionnaire-24hfood"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class QInsideTracker(flask.views.MethodView):
	@utils.login_required
	def get(self, page="input-insidetracker"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)