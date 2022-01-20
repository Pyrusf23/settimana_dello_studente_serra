from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms.loginForm import LoginForm
from forms.registrazioneForm import RegistrazioneForm
from models.db import db
from models.User import User
from flask_login import login_user, current_user, logout_user, login_required


# Settings
dashboard = Blueprint('dashboard', __name__)

# Routing
@dashboard.route("/attivita")
@login_required
def activities():

    return render_template("attivita.html", user=current_user.email)