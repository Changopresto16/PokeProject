from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from .models import db


from .auth.authroutes import auth
#from .Trainers.trainroute import Trainers 
from .models import User

app = Flask(__name__)
login = LoginManager()

@login.user_loader
def load_user(id):
    return User.query.get(id)


app.register_blueprint(auth)
#app.register_blueprint(Trainers)
app.config.from_object(Config)

from.models import db

db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)


login.login_view = 'auth.logMeIn'


from . import routes
from . import models