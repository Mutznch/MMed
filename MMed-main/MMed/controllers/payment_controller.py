from flask import Blueprint, render_template, request, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from models import User, Doctor

payment = Blueprint("payment", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@payment.route("./")
@login_required
def payment_index():
    return render_template("/payment_index.html")

@payment.route("./credit_card")
@login_required
def payment_credit():
    return render_template("/payment_credit.html")

@payment.route("./debit_card")
@login_required
def payment_debit():
    return render_template("/payment_debit.html")

@payment.route("./pix")
@login_required
def payment_pix():
    return render_template("/payment_pix.html")



