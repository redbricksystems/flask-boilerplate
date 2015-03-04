import datetime
from main_app import app
from flask.ext.security import UserMixin, RoleMixin
#from main_app.core import db
from flask.ext.mongoengine import MongoEngine

db = MongoEngine(app)

class Role(db.Document, RoleMixin):

    #Default fields in Flask-secuirty
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):

    #Default fields in Flask-secuirty
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])

    #Optional/Additional fields for Registration
    first_name = db.StringField(max_length=255)
    last_name = db.StringField(max_length=255)

    #Field >confirmed_at is required for email confirmation when setting
    #SECURITY_CONFIRMABLE = True in Flask-secuirty configs
    confirmed_at = db.DateTimeField()

    #These fields are required for tracking user login info when setting
    #SECURITY_TRACKABLE = True in Flask-secuirty configs
    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField()
    current_login_ip = db.StringField()
    login_count = db.IntField()

class Posts(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now)
    title = db.StringField(verbose_name="title", max_length=255, required=True)
    post = db.StringField(verbose_name="Content", required=True)
    author_id = db.StringField(verbose_name="A uthor_Id", required=True)

class Comments(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now)
    comment = db.StringField(verbose_name="Content", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)
    post_id = db.StringField(verbose_name="Author_Id", required=True)

