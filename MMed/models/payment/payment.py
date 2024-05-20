from models import db, Patient, Clinic

class Payment(UserMixin, db.Model):
    __tablename__ = "payments"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    clinic_id = db.Column(db.Integer(), db.ForeignKey(Clinic.id))
    value = db.Column(db.Float(), nullable=False)
    form = db.Column(db.String(30), nullable=False)