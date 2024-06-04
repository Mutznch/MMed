from models import db, User

class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))

    def get_admin_by_id(id):
        return Admin.query.filter_by(id=id).first()

    def get_admin_by_user_id(user_id):
        admin = Admin.query.filter_by(user_id=user_id).first()

        return admin

    def delete_admin(id):
        try:
            Admin.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False