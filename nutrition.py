import flask, flask.views
import os
import utils
from itertools import izip

class Nutrition(flask.views.MethodView):
	@utils.login_required	
	def get(self, page="nutrition"):
		# Nutrition data
		x = {'date':[u'2012-06-27', u'2012-06-28', u'2012-06-29', u'2012-06-30'], 'users': [405, 368, 119, 11]};
		x2 = [dict(date=d, user=u) for d, u in izip(x['date'], x['users'])];

		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page, x=x2)
		flask.abort(404)

# class coachNutrition(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="coach-nutrition"):
# 		page += ".html"
# 		if os.path.isfile('templates/' + page):
# 			return flask.render_template(page)
# 		flask.abort(404)

# class clientNutrition(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="client-nutrition"):
# 		page += ".html"
# 		if os.path.isfile('templates/' + page):
# 			return flask.render_template(page)
# 		flask.abort(404)

# class gformNutrition(flask.views.MethodView):
# 	@utils.login_required
# 	def get(self, page="gformNutrition"):
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