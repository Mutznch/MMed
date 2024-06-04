from models import db, HealthInsuranceCompany

class HealthInsurance(db.Model):
    __tablename__ = "healthInsurances"
    id = db.Column("id", db.Integer(), primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey(HealthInsuranceCompany.id))
    name = db.Column(db.String(30), nullable=False)
    maximum_cover = db.Column(db.Float(), nullable=False)

    health_insurance_contracts = db.relationship("HealthInsuranceContract", backref="healthInsurances", lazy=True)

    def save_health_insurance(company_id, name, maximum_cover):
        healthInsurance = HealthInsurance(company_id=company_id, name=name, maximum_cover=maximum_cover)

        db.session.add(healthInsurance)
        db.session.commit()

    def get_health_insurance_by_id(id):
        return HealthInsurance.query.filter_by(id=id).first()
    
    def get_company_health_insurances(company_id):
        return HealthInsurance.query.filter_by(company_id=company_id).all()

    def delete_clinic(id):
        try:
            HealthInsurance.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False