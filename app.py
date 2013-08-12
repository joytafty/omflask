import os
from flask import Flask, render_template, send_from_directory, Response, url_for, request
import json

# Views
from main import Main
from login import Login, Logout, Signup
from profile import Profile
# from gform import Qpreboarding, Qonboarding, Q24hfood, QInsideTracker
from physical import Physical
# from physical import Physical, coachPhysical, clientPhysical, gformPhysical, gres
from nutrition import Nutrition
# from nutrition import Nutrition, coachNutrition, clientNutrition, gformNutrition
from activity import Activity
# from activity import Activity, coachActivity, clientActivity, gformActivity
# from charts import Charts
from d3charts import d3Charts,dcCharts
#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)
app.config.from_object('config')
app.config.update(
	DEBUG = True,
)

app.config["SECRET_KEY"] = 'T\x9cs;\x8b\xce-@\xac\xbb\xc9m\xeb\xe8\x1f\x85]\xd2M\xf5\xae$I\x9a'
### marker for flask app generator - keep this line


#----------------------------------------
# controllers
#----------------------------------------

# @app.route('/favicon.ico')
# def favicon():
# 	return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

# Routes    
# Static main view
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])

# Dynamic URL rule
# List of forms
# 1. Preboarding questionaire
# 2. Onboarding questionaire
# 3. 

# List of view 
# 0. Login
# 1. Welcome/Goal 
# 2. Physical Measurements ()
# 3. Physical Activity
# 4. Diet/Nutrition
# 5. Cardiovascular Health
# 6. Blood Work
# 7. Aging (Longevity)

app.add_url_rule('/signin/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/logout/',
                 view_func=Logout.as_view('logout'),
                 methods=["GET", "POST"])
app.add_url_rule('/signup/',
                 view_func=Signup.as_view('signup'),
                 methods=["GET"])

# Welcome page
# app.add_url_rule('/welcome/',
#                  view_func=Welcome.as_view('welcome'),
#                  methods=["GET", "POST"])

app.add_url_rule('/user-profile/',
                 view_func=Profile.as_view('profile'),
                 methods=["GET"])

# # Form Views
# app.add_url_rule('/questionaire/preboarding/',
#                  view_func=Qpreboarding.as_view('questionnaire-preboarding'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/questionaire/onboarding/',
#                  view_func=Qonboarding.as_view('questionnaire-onboarding'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/questionaire/24hfood/',
#                  view_func=Q24hfood.as_view('questionnaire-24hfood'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/input/insidetracker/',
#                  view_func=QInsideTracker.as_view('input-insidetracker'),
#                  methods=["GET", "POST"])

# Physical Measurements Views
app.add_url_rule('/physical/',
                 view_func=Physical.as_view('physical'),
                 methods=["GET", "POST"])
app.add_url_rule('/activity/',
                 view_func=Activity.as_view('activity'),
                 methods=["GET", "POST"])
app.add_url_rule('/nutrition/',
                 view_func=Nutrition.as_view('nutrition'),
                 methods=["GET", "POST"])


# app.add_url_rule('/coach/physical/',
#                  view_func=coachPhysical.as_view('coach-physical'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/client/physical/',
#                  view_func=clientPhysical.as_view('client-physical'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/gformPhysical/',
#                  view_func=gformPhysical.as_view('gformphysical'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/gres/',
#                  view_func=gres.as_view('gres'),
#                  methods=["GET", "POST"])

# # Nutrition Views
# app.add_url_rule('/nutrition/',
#                  view_func=Nutrition.as_view('nutrition'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/coach/nutrition/',
#                  view_func=coachNutrition.as_view('coach-nutrition'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/client/nutrition/',
#                  view_func=clientNutrition.as_view('client-nutrition'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/gformNutrition/',
#                  view_func=gformNutrition.as_view('gformnutrition'),
#                  methods=["GET", "POST"])

# # Activity Views
# app.add_url_rule('/activity/',
#                  view_func=Activity.as_view('activity'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/coach/activity/',
#                  view_func=coachActivity.as_view('coach-activity'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/client/activity/',
#                  view_func=clientActivity.as_view('client-activity'),
#                  methods=["GET", "POST"])
# app.add_url_rule('/gformNutrition/',
#                  view_func=gformActivity.as_view('gformactivity'),
#                  methods=["GET", "POST"])


# # Chart Views
# app.add_url_rule('/charts/',
#                  view_func=Charts.as_view('charts'),
#                  methods=["GET", "POST"])
app.add_url_rule('/d3charts/',
                 view_func=d3Charts.as_view('d3charts'),
                 methods=["GET", "POST"])
app.add_url_rule('/dcindex/',
                 view_func=dcCharts.as_view('dcindex'),
                 methods=["GET", "POST"])

#----------------------------------------
# handlers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/optmeico.ico')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#----------------------------------------
# database
#----------------------------------------
from mongoengine import connect
from flask.ext.mongoengine import MongoEngine

# Mongo Lab Database connection
# DB_NAME = 'jrflask'
# DB_USERNAME = 'jrflaskadmin'
# DB_PASSWORD = 'jrflask12345'
# DB_HOST_ADDRESS = 'ds031278.mongolab.com:31278/jrflask'
# app.config["MONGODB_DB"] = DB_NAME
# connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)

# MongoHQ Database connection
DB_NAME = 'app15407585'
DB_USERNAME = 'heroku'
DB_PASSWORD = '6cefeffb1806c2444c074e4b680ff76f'
DB_HOST_ADDRESS = 'ethan.mongohq.com'
DB_PORT = 10031
app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, 
	username=DB_USERNAME,
	password=DB_PASSWORD,
	host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS + ':' + str(DB_PORT) + '/' + DB_NAME,
	port=DB_PORT,
)

db = MongoEngine(app)


#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)