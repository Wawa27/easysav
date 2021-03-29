from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from easysav.controllers import interventions
from easysav.controllers import home

app.route(interventions)
app.route(home)
