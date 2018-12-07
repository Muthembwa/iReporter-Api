#user_models.py
from flask_bcrypt import Bcrypt


class userModel()
    Users = [
        {
        "id" : "Integer", 
        "firstname" : String,
        "lastname" : String,
        "othernames" : String,
        "email" : String,
        "phoneNumber" : String,
        "username" : String, 
        "registered" : Date,
        "isAdmin ": Boolean,
        
        }  ]

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin