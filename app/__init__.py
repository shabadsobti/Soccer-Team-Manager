from flask import Flask
import os

app = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'), instance_relative_config = True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
print app.config['SECRET_KEY']


from app import views
