import flask, flask.views
import os
import utils

class Nutrition(flask.views.MethodView):
	@utils.login_required
	def get(self, page="nutrition"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class coachNutrition(flask.views.MethodView):
	@utils.login_required
	def get(self, page="coach-nutrition"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class clientNutrition(flask.views.MethodView):
	@utils.login_required
	def get(self, page="client-nutrition"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class gformNutrition(flask.views.MethodView):
	@utils.login_required
	def get(self, page="gformNutrition"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class gres(flask.views.MethodView):
	@utils.login_required
	def get(self, page="gres"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)