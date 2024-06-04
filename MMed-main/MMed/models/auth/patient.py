from models import db, User

class Patient(db.Model):
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
        patient = Patient(user_id=user_id, name=name)

        db.session.add(patient)
        db.session.commit()

    def get_patient_by_user_id(user_id):
        patient = Patient.query.filter_by(user_id=user_id).first()

        return patient

    def delete_patient(id):
        try:
            Patient.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False