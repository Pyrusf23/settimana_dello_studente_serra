from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

main = Blueprint("main", __name__)

@main.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for('auth.login'))
        #return render_template("index.html", user=current_user.email)
    return redirect(url_for('auth.login'))
    #return render_template("index.html")

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404