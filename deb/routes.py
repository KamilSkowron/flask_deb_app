from deb import app, db
from flask import render_template, redirect, url_for, request
from deb.restAPI import DebsAPI
from deb.forms import LoginForm, DebForm
from deb.models import User, Deb_info
from flask_login import login_user, current_user, logout_user, login_required


debs = DebsAPI()

@app.route('/home',methods=['GET','POST'])
@login_required
def start_page():
    form = DebForm()

    if request.method == "POST":
        
        #Read Form
        borrower = request.form['borrower']
        amount = request.form['amount']
        description = request.form['description']
        debtor = current_user.username

        #Clear Form
        form.amount.data = ""
        form.borrower.data = ""
        form.description.data = ""

        if request.form['action'] == 'Add Deb':
            deb = Deb_info(debtor=debtor,borrower=borrower, description=description, amount=amount)

        elif request.form['action'] == 'Reduse Deb':
            deb = Deb_info(debtor=debtor,borrower=borrower, description=description, amount="-"+amount)
    
        db.session.add(deb)
        db.session.commit()
        return redirect(url_for('start_page'))
    
    return render_template('main.html',debs=debs.get()[0], form=form )


@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/login_page',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        print(attempted_user)
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            print("LOGGIN")
            print(attempted_user.username)
            return redirect(url_for('start_page'))

    return render_template('login.html',form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    print("LOGOUT")
    return redirect(url_for("start_page"))

