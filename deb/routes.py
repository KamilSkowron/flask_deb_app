from deb import app
from flask import render_template
from deb.restAPI import DebsAPI
from deb.forms import LoginForm

debs = DebsAPI()

@app.route('/home')
def start_page():
	return render_template('main.html',debs=debs.get()[0])


@app.route('/register_page')
def register_page():
	return render_template('register.html')

@app.route('/login_page',methods=['GET','POST'])
def login_page():
	form = LoginForm()
	if form.submit():
		print("SUB")

	if form.validate_on_submit():
		print("KSAKS")
	return render_template('login.html',form=form)