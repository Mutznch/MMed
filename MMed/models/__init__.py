from models.db import db, instance
from models.auth.user import User
from models.auth.admin import Admin
from models.auth.patient import Patient
from models.auth.doctor import Doctor

from models.auth.clinic import Clinic
from models.auth.role import Role

from models.auth.healthInsurance import HealthInsurance
from models.auth.healthInsurance import HealthInsuranceCompany
from models.auth.healthInsurance import HealthInsuranceContract

from models.auth.payment import Payment

from models.auth.schedule import Appointment
from models.auth.schedule import Exam