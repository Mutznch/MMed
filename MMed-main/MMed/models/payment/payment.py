from models import db, Patient, Clinic, User

class Payment(db.Model):
    __tablename__ = "payments"
    id = db.Column("id", db.Integer(), primary_key=True)
    patient_id = db.Column(db.Integer(), db.ForeignKey(Patient.id))
    clinic_id = db.Column(db.Integer(), db.ForeignKey(Clinic.id))
    value = db.Column(db.Float(), nullable=False)
    form = db.Column(db.String(30), nullable=False)

    def save_payment(patient_id, clinic_id, value, form):

        payment = Payment(patient_id=patient_id, clinic_id=clinic_id, value=value, form=form)

        db.session.add(payment)
        db.session.commit()

    def get_payment_by_id(id):
        return Payment.query.filter_by(id=id).first()
    
    def get_patient_payments(patient_id):
        return Payment.query.filter_by(patient_id=patient_id)\
            .join(Clinic, Clinic.id == Payment.clinic_id)\
            .add_columns(Payment.id, Clinic.name, Payment.value, Payment.form)\
            .all()
    
    def get_clinic_payments(clinic_id):
        return Payment.query.filter_by(clinic_id=clinic_id)\
            .join(Patient, Patient.id == Payment.patient_id)\
            .join(User, User.id == Patient.userId)\
            .add_columns(Payment.id, User.name, Payment.value, Payment.form)\
            .all()

    def delete_payment(id):
        try:
            Payment.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False