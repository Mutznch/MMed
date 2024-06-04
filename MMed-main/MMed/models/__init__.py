from models.db import db, instance
from models.auth.user import User
from models.auth.admin import Admin
from models.auth.patient import Patient
from models.auth.doctor import Doctor

from models.clinic.clinic import Clinic
from models.clinic.role import Role

from models.healthInsurance.healthInsuranceCompany import HealthInsuranceCompany
from models.healthInsurance.healthInsurance import HealthInsurance
from models.healthInsurance.healthInsuranceContract import HealthInsuranceContract

from models.payment.payment import Payment

from models.schedule.appointment import Appointment
from models.schedule.exam import Exam