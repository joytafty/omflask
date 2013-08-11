import flask, flask.views
import os
import utils
from itertools import izip

class Physical(flask.views.MethodView):
	@utils.login_required

	def get(self, page="physical"):

		x1 = {'measure': [u'height', u'weight', u'waist circumference', u'bodyfat'],
			'yours': [u'6 feet', u'160 lbs', u'32 inches', u'12.5%'],
			'ideal': [u' N/A ', u'150-170 lbs', u'28-36 inches', u'10-15%']}
		# x1 = {'category': [u'your measure', u'ideal range'],
		# 	'bh' : [u'6 feet', u''],
		# 	'bw' : [u'160 lbs', u'150-170 lbs'],
		# 	'waist' : [u'32 inches', u'28-36 inches'],
		# 	'bodyfat' : [u'13%', u'10-15%']
		# }		
		x1 = [dict(measure=m,yours=y,ideal=i) for m,y,i in izip(x1['measure'], x1['yours'], x1['ideal'])]
			# dat2 = [
   #    		['Date', 'Your Measure', 'Category0', 'Category1', 'Category 2', 'Category 3', 'Category 4'],
   #    		['current date', 29.0, 18.5, 6.3, 4.9, 4.9, 9.0],
   #    		['new date 1', 24.0, 18.5, 6.3, 4.9, 4.9, 9.0],	
   #    		['new date 2', 21.2, 18.5, 6.3, 4.9, 4.9, 9.0],	
   #    		['new date 3', 20.2, 18.5, 6.3, 4.9, 4.9, 9.0]	
   #    		]);
			
			# dat3 = [
	  #   	['Date', 'Your Measure', 'Essential', 'Athelete', 'Fit', 'Average', 'Above Average'],
   #  		['current date', 20.0, 5.0, 8.0, 4.0, 6.0, 9.0],
   #  		['new date 1', 15.0, 5.0, 8.0, 4.0, 6.0, 9.0], 
   #  		['new date 2', 12.2, 5.0, 8.0, 4.0, 6.0, 9.0], 
   #  		['new date 3', 10.2, 5.0, 8.0, 4.0, 6.0, 9.0]  
   #  		]);

		page += ".html"
		if os.path.isfile('templates/' + page):
			return flask.render_template(page, x1=x1)
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
