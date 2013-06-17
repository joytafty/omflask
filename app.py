import os
from flask import Flask, render_template, send_from_directory, Response, url_for, request
import json

#----------------------------------------
# initialization
#----------------------------------------

app = Flask(__name__)

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

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route("/")
def index():
	return render_template('index.html')

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

DB_NAME = 'jrflask'
DB_USERNAME = 'jrflaskadmin'
DB_PASSWORD = 'jrflask12345'
DB_HOST_ADDRESS = 'ds031278.mongolab.com:31278/jrflask'

app.config["MONGODB_DB"] = DB_NAME
connect(DB_NAME, host='mongodb://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST_ADDRESS)
db = MongoEngine(app)

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)