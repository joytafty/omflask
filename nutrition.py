import flask, flask.views
import os
import utils
from itertools import izip

class Nutrition(flask.views.MethodView):
	@utils.login_required	
	def get(self, page="nutrition"):
		# Nutrition data, will later load from file
		x = {
			'Nutrient': [u'Calories (kcals)', u'Fat (g)', u'Saturdated Fat (g)', u'Protein (g)', u'Carbohygrate (g)', u'Fiber (g)', u'Sodium (mg)'], 
			'Intake': [1530, 10, 1, 0, 10, 10, 300],
			'Need': [1800, 10, 10, 10, 10, 10, 1000]}

		x['Difference'] = [x1 - x2 for (x1, x2) in zip(x['Need'], x['Intake'])]
		x2 = [dict(Nutrient=n, Intake=i, Need=r, Difference=d) for n,i,r,d in izip(x['Nutrient'], x['Intake'], x['Need'], x['Difference'])]

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