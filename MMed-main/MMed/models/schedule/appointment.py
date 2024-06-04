from models import db, Patient, Doctor
from datetime import datetime

class Appointment(db.Model):
    __tablename__ = "appointment"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    doctor_id = db.Column(db.Integer(), db.ForeignKey(Doctor.id))
    time_of_appointment = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    appointment_date = db.Column(db.DateTime(), nullable=False)

    def save_appointment(patient_id, doctor_id, appointment_date):
        appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, appointment_date=appointment_date)

        db.session.add(appointment)
        db.session.commit()

    def get_appointment_by_id(id):
        return Appointment.query.filter_by(id=id).first()

    def delete_appointment(id):
        try:
            Appointment.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False