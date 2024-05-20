from models import db, Doctor, Clinic

class Role(UserMixin, db.Model):
    __tablename__ = "roles"
    id = db.Column("id", db.Integer(), primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey(Doctor.id))
    clinic_id = db.Column(db.Integer(), db.ForeignKey(Clinic.id))
    role = db.Column(db.String(30), nullable=False, default="Multirole")