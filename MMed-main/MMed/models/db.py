from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
instance = "sqlite:///mmed"
#instance = "mysql+pymysql://mmed:123@localhost:3306/mmed"