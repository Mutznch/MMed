from models import db

class Appointment(UserMixin, db.Model):
    __tablename__ = "appointment"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    doctor_id = db.Column(db.Integer(), db.ForeignKey(Doctor.id))
    appointment_date = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    date_time = db.Column(db.DateTime(), nullable=False)
