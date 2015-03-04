from flask.ext.wtf import Form
from flask_security.forms import RegisterForm, ConfirmRegisterForm

from wtforms.fields import TextField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo

#Extended Flask-Security RegisterForm fields
class ExtendedRegisterForm(RegisterForm, ConfirmRegisterForm):
    first_name = TextField('First Name', [Required()])
    last_name = TextField('Last Name', [Required()])

class PostsForm(Form):
    author = TextField('Author', [Required()])
    post = TextField('Post', [Required()])

class CommentsForm(Form):
    comment = TextField('Comment', [Required()])
    author = TextField('Author', [Required()])

