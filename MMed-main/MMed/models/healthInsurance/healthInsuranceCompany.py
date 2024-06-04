from models import db

class HealthInsuranceCompany(db.Model):
    __tablename__ = "healthInsuranceCompanies"
    id = db.Column("id", db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    health_insurances = db.relationship("HealthInsurance", backref="healthInsuranceCompanies", lazy=True)

    def save_health_insurance_company(name):

        clinic = HealthInsuranceCompany(name=name)

        db.session.add(clinic)
        db.session.commit()

    def get_health_insurance_company_by_id(id):
        return HealthInsuranceCompany.query.filter_by(id=id).first()

    def delete_health_insurance_company(id):
        try:
            HealthInsuranceCompany.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False