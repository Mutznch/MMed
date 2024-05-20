from models import db, HealthInsuranceCompany

class HealthInsurance(UserMixin, db.Model):
    __tablename__ = "healthInsurances"
    id = db.Column("id", db.Integer(), primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey(HealthInsuranceCompany.id))
    name = db.Column(db.String(30), nullable=False)
    maximum_cover = db.Column(db.Float(), nullable=False)

    health_insurance_contracts = db.relationship("HealthInsuranceContract", backref="healthInsurances", lazy=True)