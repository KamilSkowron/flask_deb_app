from deb import api, db
from deb.models import Deb_info, User
from flask_restx import Resource
from flask import request


@api.route('/api/debs')
class DebsAPI(Resource):
    def get(self):
        debs = Deb_info.query.all()
        debs_data = [deb.to_dict() for deb in debs]
        return debs_data, 200
    

    def post(self):
        data = request.get_json()
        debtor = data.get('debtor')
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
        users = Deb_info.query.all()
        users_data = [user.to_dict() for user in users]
        return users_data, 200
    

    def post(self):
        data = request.get_json()
        username = data.get('username')
        email_address = data.get('email_address')
        password = data.get('password')
 


        deb = User(username=username,password=password,email_address=email_address)

        db.session.add(deb)
        db.session.commit()

        return deb.to_dict(), 201