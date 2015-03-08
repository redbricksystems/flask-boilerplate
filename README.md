# Flask Boilerplate app with user managment system

###Introduction
Flask is a microframework for web development written in Python. It's very easy to use and is very powerful. We created a simple Flask-Boilerplate app that you can use to quickly get started with your first project. The particular app has the capability of registering users. Each user can publish a post and comment.

###Packages included
####Flask-Security
Flask-Security allows you to quickly add common security checks to your Flask application. It includes:

- Session based authentication
- Role management
- Password encryption
- Basic HTTP authentication
- Token based authentication
- Token based account activation (optional)
- Token based password recovery / resetting (optional)
- User registration (optional)
- Login tracking (optional)
- JSON/Ajax Support

####Flask-WTF Forms
WTF Forms is a package that is frequently used in many Flask applications. It includes:

- Integration with wtforms
- Secure Form with csrf token
- Global csrf protection
- Recaptcha supporting
- File upload that works with Flask-Uploads
- Internationalization integration

####Flask Mongoengine
MongoEngine is an Object-Document Mapper, written in Python for working with MongoDB. We used mongoengine in our app to add/fetch data from MongoDB. Alternatively you can use PyMongo as well.

###Quick Start
####1. Clone the repo
Fisrt of al you'll need to clone the repo into your working directory and then cd into Flask-Boilerplate.

    $ git clone https://github.com/redbricksystems/flask-boilerplate.git
    $ cd flask-boilerplate
    
####2. Create and activate a virtualenvironment
After cloning the repo you'll have to create a virtual environment for your project and activate it using the following commands:

    $ virtualenv venv
    $ . venv/bin/activate   (for Ubuntu/Linux)
    $ cd venv, cd Script, activate (for windows)

####3. Configuration

Now in order to configure the repo, cd into the *main_app* and open up *settings.py* in your favorite text editor.

######Database Configuration
Add your database credentials

    ...
    #--------DB Config------------
    MONGODB_SETTINGS = {
    'DB':  'DB_NAME',
    'USERNAME': 'DB_USERNAME',
    'PASSWORD': 'DB_PASSWORD',
    'HOST': 'HOST_LINK',
    'PORT': PORT
    }
    ...
    
######Mail Configuration
Enter your email account information here for sending notifications such as registring/account-activation/reset-passwod via this account.

	...
    #--------Mail Config---------
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'YOUR_EMAIL'
    MAIL_PASSWORD = 'YOUR_EMAIL_PASSWORD'
    ...

######Default Routes Configuration
You can change any of the default routes here in *settings.py*. You can change them according to your need. These html templates can be found under /main_app/templates directory.

####4. Install the dependencies
Now after configuring your settings, its time to install all the required dependencies for the project. Run the following command to do so:

`$ pip install -r requirements.txt`

####5. Run the server
Run the following command to start the development server:

`$ python manage.py runserver`

####6. Open in your web browser
Open your web browser and navigate to **localhost:5000** and you'll see the running app. You can register and login via the main page. After login you can also add posts and comments.

###What's Next?

- Adding Bootstrap to your flask app
- Adding update/delete function on posts
- Deploy your flask app on heroku
- Deploy using apache
- Adding unit tests by using Python Nose package
