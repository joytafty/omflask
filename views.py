from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

# index view function suppressed for brevity

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    	flash('Login requested for' + form.openid.data + 'remember_me=' + str(form.remember_me.data))
    	return redirect('/')
    return render_template('login.html', 
        title = 'Sign In',
        form = form)