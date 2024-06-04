from models import db, Patient, HealthInsurance

class HealthInsuranceContract(db.Model):
    __tablename__ = "healthInsuranceContracts"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    health_insurance_id = db.Column(db.Integer(), db.ForeignKey(HealthInsurance.id))

    def save_health_insurance_contract(patient_id, health_insurance_id):

        health_insurance_contract = HealthInsuranceContract(patient_id=patient_id, health_insurance_id=health_insurance_id)

        db.session.add(health_insurance_contract)
        db.session.commit()

    def get_health_insurance_contract_by_id(id):
        return HealthInsurance.query.filter_by(id=id).first()

    def get_patient_health_insurance(patient_id):
        return HealthInsuranceContract.query.filter_by(patient_id=patient_id)\
            .join(HealthInsurance, HealthInsurance.id == HealthInsuranceContract.health_insurance_id)\
            .add_columns(HealthInsuranceContract.id, HealthInsurance.name, HealthInsurance.maximum_cover)\
            .all()

    def delete_health_insurance_contract(id):
        try:
            HealthInsurance.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False