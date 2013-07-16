import os
from flask import Flask, render_template, send_from_directory, Response, url_for, request
import json

# Views
from main import Main
from login import Login
from about import About
from plans import Plans
from charts import Charts
from d3charts import d3Charts
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
# Static main view
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
# Dynamic URL rule
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])
app.add_url_rule('/plans/',
                 view_func=Plans.as_view('plans'),
                 methods=["GET", "POST"])
app.add_url_rule('/about/',
                 view_func=About.as_view('about'),
                 methods=["GET", "POST"])
app.add_url_rule('/charts/',
                 view_func=Charts.as_view('charts'),
                 methods=["GET", "POST"])
app.add_url_rule('/d3charts/',
                 view_func=d3Charts.as_view('d3charts'),
                 methods=["GET", "POST"])

# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('404.html'), 404

# @app.route("/")
# def index():
# 	return render_template('index.html')

# @app.route("/about")
# def about():
# 	return render_template('about.html')

# @app.route("/plans")
# def plans():
# 	return render_template('plans.html')	
#----------------------------------------
# handlers
#----------------------------------------

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

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