import flask, flask.views
import os
import utils

class Activity(flask.views.MethodView):
	@utils.login_required
	def get(self, page="activity"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class coachActivity(flask.views.MethodView):
	@utils.login_required
	def get(self, page="coach-activity"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class clientActivity(flask.views.MethodView):
	@utils.login_required
	def get(self, page="client-activity"):
		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page)
		flask.abort(404)

class gformActivity(flask.views.MethodView):
	@utils.login_required
	def get(self, page="gformActivity"):
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