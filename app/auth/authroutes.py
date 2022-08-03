from click import confirm
from app.models import db
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .authforms import LoginForm, UserCreationForm, EditProfileForm


from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app.models import db

from app.models import User

auth = Blueprint('auth', __name__, template_folder='authtemplates')


@auth.route('/login', methods=["GET", "POST"])
def logMeIn():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
            
            if user:

                if check_password_hash(user.password, password):
                    flash('You have successfully logged in!', 'success')
                    login_user(user)
            else:
                    flash('Incorrect username/password combination.', 'danger')
        else:
                flash('User with that username does not exist.', 'danger')

    return render_template('login.html', form=form)

@auth.route('/logout')
def logMeOut():
    flash("Successfully logged out.", 'success')
    logout_user()
    return redirect(url_for('auth.logMeIn'))

@auth.route('/signup', methods=["GET", "POST"])
def signMeUp():
    form = UserCreationForm()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            


            user = User(username, email, password)


            db.session.add(user)
            db.session.commit()
            flash("Successfully registered a new user", 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Invalid form. Please fill it out correctly.', 'danger')
    return render_template('signup.html', form = form)

@auth.route('/editprofile', methods=["GET", "POST"])
def EditProfile():
    form = EditProfileForm()
    user = User.query.get(current_user.id)
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data



            user.username = username
            user.email = email
            db.session.commit()

            flash("Successfully changed info", 'success')
            return redirect(url_for('auth.EditProfile'))
        else:
            flash('Invalid form. Please fill it out correctly.', 'danger')
    return render_template('editprofile.html', form = form, user = user)
