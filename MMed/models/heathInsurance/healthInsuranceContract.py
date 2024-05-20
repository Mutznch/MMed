from models import db, Patient, HealthInsurance

class HealthInsuranceContract(UserMixin, db.Model):
    __tablename__ = "healthInsuranceContracts"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    health_insurance_id = db.Column(db.Integer(), db.ForeignKey(HealthInsurance.id))