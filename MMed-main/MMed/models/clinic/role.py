from models import db, Doctor, Clinic, User

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column("id", db.Integer(), primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey(Doctor.id))
    clinic_id = db.Column(db.Integer(), db.ForeignKey(Clinic.id))
    role = db.Column(db.String(30), nullable=False, default="Multirole")

    def save_role(doctor_id, clinic_id, role):
        role = Role(doctor_id=doctor_id, clinic_id=clinic_id, role=role)

        db.session.add(role)
        db.session.commit()

    def get_role_by_id(id):
        role = Role.query.filter_by(id=id)

        return role
    
    def get_clinic_doctors(clinic_id):
        return Role.query.filter_by(clinic_id=clinic_id)\
            .join(Doctor, Doctor.id == Role.doctor_id)\
            .join(User, User.id == Doctor.userId)\
            .add_columns(Doctor.id, User.name, Role.role)\
            .all()
    
    def get_doctor_clinics(doctor_id):
        return Role.query.filter_by(doctor_id=doctor_id)\
            .join(Clinic, Clinic.id == Role.clinic_id)\
            .add_columns(Clinic.id, Clinic.name, Role.role)\
            .all()

    def delete_role(id):
        try:
            Role.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False