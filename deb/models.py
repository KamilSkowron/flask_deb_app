from deb import db, bcrypt, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=60), nullable=False)
    last_name = db.Column(db.String(length=60), nullable=False)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    debs = db.relationship('Deb_info', backref='debs_user', lazy=True)


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def to_dict(self):
        return {"id": self.id,"first_name": self.first_name,"last_name": self.last_name, "username": self.username, "email_address": self.email_address, "password_hash": self.password_hash}

class Deb_info(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    borrower = db.Column(db.String(length=30), nullable=False)
    description = db.Column(db.String(length=1024),
                            nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    debtor = db.Column(db.String(length=30), db.ForeignKey('user.id'))


    def to_dict(self):
        return {"id": self.id, "debtor": self.debtor, "borrower": self.borrower, "description": self.description, "amount": self.amount, "date_added": f'{self.date_added}'[:19]}

    def __repr__(self):
        return [self.debtor, self.borrower, self.amount]



db.create_all()