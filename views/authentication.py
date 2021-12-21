from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms.loginForm import LoginForm
from forms.registerForm import RegistrazioneForm
from models import db, User
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, logout_user, login_required


# Settings
auth = Blueprint('auth', __name__)

# Routing
@auth.route("/registrazione", methods=('GET', 'POST'))
def registrazione():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrazioneForm()

    if form.validate_on_submit() and request.method == 'POST':
        email = form.email.data
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        query = User(email, username, password, remember)
        db.session.add(query)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('registrazione.html', form=form)

@auth.route("/login", methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()

    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('main.index'))
            else: flash('Credenziali errate!')
        else: flash('Credenziali errate!')
    
    return render_template('login.html', form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
