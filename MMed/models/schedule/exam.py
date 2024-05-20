from models import db

class Exam(UserMixin, db.Model):
    __tablename__ = "exams"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    doctor_id = db.Column(db.Integer(), db.ForeignKey(Doctor.id))
    exam_type = db.Column(db.String(30), nullable=False)
    appointment_date = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    date_time = db.Column(db.DateTime(), nullable=False)