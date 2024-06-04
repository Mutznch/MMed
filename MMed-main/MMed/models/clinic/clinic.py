from models import db

class Clinic(db.Model):
    __tablename__ = "clinics"
    id = db.Column("id",  db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    role = db.relationship("Role", backref="clinics", lazy=True)
    payments = db.relationship("Payment", backref="clinics", lazy=True)

    def save_clinic(name):

        clinic = Clinic(name=name)

        db.session.add(clinic)
        db.session.commit()

    def get_clinic_by_id(id):
        return Clinic.query.filter_by(id=id).first()

    def delete_clinic(id):
        try:
            Clinic.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False