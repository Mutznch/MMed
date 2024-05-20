from models import db

class Clinic(UserMixin, db.Model):
    __tablename__ = "clinics"
    id = db.Column("id",  db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    role = db.relationship("Role", backref="clinics", lazy=True)
    payments = db.relationship("Payment", backref="clinics", lazy=True)