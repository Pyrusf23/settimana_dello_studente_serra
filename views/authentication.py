from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms.loginForm import LoginForm
from forms.registrazioneForm import RegistrazioneForm
from models import db, User
from flask_login import login_user, current_user, logout_user, login_required


# Settings
auth = Blueprint('auth', __name__)

# Routing
@auth.route("/registrazione", methods=('GET', 'POST'))
def registrazione():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.activities'))
    form = RegistrazioneForm()

    if form.validate_on_submit() and request.method == 'POST':
        try:
            email = form.email.data + "@isisserra.edu.it"
            password = form.password.data
            query = User(email, password, form.class_id.data)
            db.session.add(query)
            db.session.commit()
            login_user(query, remember=form.remember.data)
            return redirect(url_for('main.index'))
        except: flash('Utente già registrato')

    return render_template('registrazione.html', form=form)

@auth.route("/login", methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.activities'))
    form = LoginForm()

    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.verifyPassword(form.password.data):
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
