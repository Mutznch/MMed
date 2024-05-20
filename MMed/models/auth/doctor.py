from models import db, User

class Doctor(UserMixin, db.Model):
    __tablename__ = "doctors"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))

    role = db.relationship("Role", backref="doctors", lazy=True)
    appointments = db.relationship("Appointment", backref="doctors", lazy=True)
    exams = db.relationship("Exam", backref="doctors", lazy=True)