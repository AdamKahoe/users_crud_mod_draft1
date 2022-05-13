import imp
from flask_app import app
from flask_app.controllers import controllers_users
# from flask_app.config import mysqlconnection
# from flask_app.models import models_users

if __name__=="__main__":
    app.run(debug=True)