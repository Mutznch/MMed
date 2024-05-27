from models import db, User

class Admin(UserMixin, db.Model):
    __tablename__ = "admins"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))

    def get_admin_by_id(id):
        return Admin.query.filter_by(id=id).first()

    def isUserAdmin(user_id):
        admin = Admin.query.filter_by(user_id=user_id).first()

        return True if patient else False