from models import db

class HealthInsuranceCompany(UserMixin, db.Model):
    __tablename__ = "healthInsuranceCompanies"
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    health_insurances = db.relationship("HealthInsurance", backref="healthInsuranceCompanies", lazy=True)