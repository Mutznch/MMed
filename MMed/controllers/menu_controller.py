from flask import Blueprint, render_template, request, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from models import User, Doctor

menu = Blueprint("menu", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@menu.route("./")
@login_required
def menu_index():
    return render_template("/menu_index.html")

@menu.route("./appointments")
@login_required
def menu_appointments():
    return render_template("/menu_appointments.html")

@menu.route("./new_appointment")
@login_required
def menu_new_appointment():
    return render_template("/menu_new_appointment.html")

@menu.route("./new_exam")
@login_required
def menu_new_exam():
    return render_template("/menu_new_exam.html")

@menu.route("./update")
@login_required
def menu_new_exam():
    return render_template("/menu_update.html")

#DOCTOR

@menu.route("./doctor")
@login_required
def menu_doctor():
    if (Doctor.isUserAdmin(current_user.id)): 
        return render_template("doctor/doctor_index.html", user=current_user)

    return render_template("/home.html")

@menu.route("./doctor/schedule")
@login_required
def menu_doctor_schedule():
    if (Doctor.isUserAdmin(current_user.id)): 
        return render_template("doctor/doctor_schedule.html", user=current_user)

    return render_template("/home.html")

@menu.route("./doctor/post_schedule")
@login_required
def menu_doctor_post_schedule():

@menu.route("./remove")
@login_required
def menu_remove():