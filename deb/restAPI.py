from deb import api, db
from deb.models import Deb_info, User
from flask_restx import Resource
from flask import request
from flask_login import current_user

@api.route('/api/debs')
class DebsAPI(Resource):
    def get(self):
        debs = Deb_info.query.all()
        debs_data = [deb.to_dict() for deb in debs]
        return debs_data, 200
    

    def post(self):
        data = request.get_json()
        debtor = data.get('debtor')
        #debtor = current_user.username
        borrower = data.get('borrower')
        description = data.get('description')
        amount = data.get('amount')


        deb = Deb_info(debtor=debtor,borrower=borrower,description=description, amount=amount)

        db.session.add(deb)
        db.session.commit()

        return deb.to_dict(), 201

@api.route('/api/users')
class UsersAPI(Resource):
    def get(self):
        users = User.query.all()
        users_data = [user.to_dict() for user in users]
        return users_data, 200
    

    def post(self):
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email_address = data.get('email_address')
        password = data.get('password')
 


        deb = User(first_name=first_name,last_name=last_name,username=username,password=password,email_address=email_address)

        db.session.add(deb)
        db.session.commit()

        return deb.to_dict(), 201