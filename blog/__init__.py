from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page')
login.login_message_category = 'info'

bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# from blog import routes, models, errors
from blog.models import User, Post

# Admin Panel
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))






