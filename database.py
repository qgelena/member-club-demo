from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Member Model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    registration_date = db.Column(db.DateTime())

    def __init__(self, name, email, registration_date=None):
        self.name = name
        self.email = email
        self.registration_date = registration_date

if __name__ == '__main__':
    from app import app
    db.create_all(app=app)