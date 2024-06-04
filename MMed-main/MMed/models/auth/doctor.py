from models import db, User

class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))

    role = db.relationship("Role", backref="doctors", lazy=True)
    appointments = db.relationship("Appointment", backref="doctors", lazy=True)
    exams = db.relationship("Exam", backref="doctors", lazy=True)

    def get_doctor_by_id(id):
        return Doctor.query.filter_by(id=id).first()

    def save_doctor(user_id, name):
        doctor = Doctor(user_id=user_id, name=name)

        db.session.add(doctor)
        db.session.commit()

    def get_doctor_by_user_id(user_id):
        doctor = Doctor.query.filter_by(user_id=user_id).first()

        return doctor

    def delete_doctor(id):
        try:
            Doctor.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False