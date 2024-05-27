from models import db, User

class Patient(UserMixin, db.Model):
    __tablename__ = "patients"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))

    health_insurance_contracts = db.relationship("HealthInsuranceContract", backref="patients", lazy=True)
    appointments = db.relationship("Appointment", backref="patients", lazy=True)
    exams = db.relationship("Exam", backref="patients", lazy=True)
    payments = db.relationship("Payment", backref="patients", lazy=True)

    def get_patient_by_id(id):
        return Patient.query.filter_by(id=id).first()

    def save_patient(user_id, name):
        patient = Patient(user_id=owner_id, name=name)

        db.session.add(patient)
        db.session.commit()

    def isUserPatient(user_id):
        patient = Patient.query.filter_by(user_id=user_id).first()

        return True if patient else False