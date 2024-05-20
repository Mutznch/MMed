from models import db, User

class Patient(UserMixin, db.Model):
    __tablename__ = "patients"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))

    health_insurance_contracts = db.relationship("HealthInsuranceContract", backref="patients", lazy=True)
    appointments = db.relationship("Appointment", backref="patients", lazy=True)
    exams = db.relationship("Exam", backref="patients", lazy=True)
    payments = db.relationship("Payment", backref="patients", lazy=True)