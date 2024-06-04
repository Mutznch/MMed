from flask import Blueprint, render_template, request, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User

admin = Blueprint("admin", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@admin.route("/")
@login_required
def auth_index():
    return render_template("admin/admin_index.html", user=current_user)
