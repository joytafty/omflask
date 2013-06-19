import flask, flask.views
import functools

def login_required(method):
	@functools.wraps(method)
	# Define wrapper
	def wrapper(*args, **kwargs):
		if 'usr' in flask.session:
			# User in session, Ok to call method
			return method(*args, **kwargs)
		else:
			flask.flash("Please log in to access your dashboard")
			return flask.redirect(flask.url_for('login'))
	return wrapper
