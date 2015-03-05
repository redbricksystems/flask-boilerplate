import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from main_app.models import Comments, Posts, User
from main_app.forms import CommentsForm, PostsForm

from flask.ext.security import login_required, current_user
#from flask.ext.security.datastore import UserDatastore
from main_app import app
from main_app.core import security
from main_app.core import security, user_datastore, db

# Create a user to test with
@app.before_first_request
def create_user():
    user_datastore.create_user(email='test@redbrick.com', password='password', first_name='first_name', last_name='last_name')

# This processor is added to all templates
@security.context_processor
def security_context_processor():
    return dict(hello="world")

# This processor is added to only the login view
@security.login_context_processor
def login_context_processor():
    return dict(test="something")

# This processor is added to all emails
@security.mail_context_processor
def security_mail_processor():
    return dict(hello="world")

# app controllers
@app.route('/')
def index():
	return render_template('index.html',
		user = current_user)

@app.route('/user-profile')
@login_required
def home():
	"""
		For adding roles to user, following functions can be use
	"""
	#my_var = {'name': 'admin', 'description': 'I am admin'}
	#role = user_datastore.find_or_create_role("admin")
	#user_datastore.add_role_to_user(current_user, role)
	#if len(current_user.roles) == 0:
	#	print "You are no access to Data files!" + str(role)
	return render_template('user_profile.html')

@app.route('/add_post', methods = ['GET', 'POST'])
@login_required
def add_post():
	form = PostsForm()
	if form.validate_on_submit():
		post = Posts(title=form.author.data, post=form.post.data, author_id=str(current_user.id))
		post.save()
	return render_template('add_post.html', 
        user = current_user,
        form = form)

@app.route('/posts')
@login_required
def show_posts():
	posts = Posts.objects
	return render_template("posts.html",
        user = current_user,
        posts = posts)

@app.route('/post/<post_id>', methods = ['GET', 'POST'])
@login_required
def show_post(post_id):
	post = Posts.objects.get_or_404(id=post_id)
	comments = Comments.objects(post_id=post_id)
	form = CommentsForm();
	if form.validate_on_submit():
		comment = Comments(author=form.author.data, comment=form.comment.data, post_id=post_id)
		comment.save()
		form.author.data = ""
		form.comment.data = ""
	return render_template("post.html",
        user = current_user,
        post = post,
       	comments = comments,
        form = form)

@app.route('/about')
def about():
    return render_template('about.html')

# special file handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
