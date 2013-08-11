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

# class coachPhysical(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="coach-physical"):
# 		page += ".html"
# 		if os.path.isfile('templates/' + page):
# 			return flask.render_template(page)
# 		flask.abort(404)

# class clientPhysical(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="client-physical"):
# 		page += ".html"
# 		if os.path.isfile('templates/' + page):
# 			return flask.render_template(page)
# 		flask.abort(404)

# class gformPhysical(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="gformPhysical"):
# 		page += ".html"
# 		if os.path.isfile('templates/' + page):
# 			return flask.render_template(page)
# 		flask.abort(404)

# class gres(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="gres"):
# 		page += ".html"
# 		if os.path.isfile('templates/' + page):
# 			return flask.render_template(page)
# 		flask.abort(404)
