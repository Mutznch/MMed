from models import db, User

class Admin(UserMixin, db.Model):
    __tablename__ = "admins"
    id = db.Column("id",  db.Integer(), primary_key=True)
    userId = db.Column(db.Integer(), db.ForeignKey(User.id))