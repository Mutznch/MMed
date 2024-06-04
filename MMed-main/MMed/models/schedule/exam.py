from models import db, Patient, Doctor
from datetime import datetime

class Exam(db.Model):
    __tablename__ = "exams"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    doctor_id = db.Column(db.Integer(), db.ForeignKey(Doctor.id))
    exam_type = db.Column(db.String(30), nullable=False)
    time_of_appointment = db.Column(db.DateTime(), nullable=False, default=datetime.now())
    appointment_date = db.Column(db.DateTime(), nullable=False)

    def save_exam(patient_id, doctor_id, exam_type, appointment_date):
        exam = Exam(patient_id=patient_id, doctor_id=doctor_id, appointment_date=appointment_date)

        db.session.add(exam)
        db.session.commit()

    def get_exam_by_id(id):
        return Exam.query.filter_by(id=id).first()

    def delete_exam(id):
        try:
            Exam.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False