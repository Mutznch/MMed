from models import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column("id",  db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    cep = db.Column(db.String(8), nullable=False)
    password = db.Column(db.String(1024), nullable=False) 
    
    def save_user(username, name, email, cpf, cep, password):

        user = User(username=username, name=name, email=email, cpf=cpf, cep=cep, password=password)

        db.session.add(user)
        db.session.commit()

    def credentials_exists(email=None, cpf=None):
        userEmail = User.query.filter_by(email=email).first()
        userCPF = User.query.filter_by(cpf=cpf).first()

        return True if (userEmail or userCPF) else False

    def validate_credentials(login, password):

        user = User.query.filter_by(email=login).first()

        return user if \
            user and \
            check_password_hash(user.password, password) \
            else None

    def get_user_by_id(id):
        return User.query.filter_by(id=id).first()
    
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()
    
    def update_user(data):
        User.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], 
                email=data['email'], 
                cpf = data['cpf'], 
                cep = data["cep"], 
                password=data['password']))
        
        db.session.commit()

    def delete_user(id):
        try:
            User.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except:
            return False
