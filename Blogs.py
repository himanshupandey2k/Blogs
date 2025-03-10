from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eef620ea683b020344456048dfa82a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(15), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.userName}', '{self.email}', '{self.image}')"

class Post(db.Model) :
    id = db.Column(db.Integer, primary_key=True)    
    title = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    content = db.Column(db.Text, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date}')"

posts = [
    { 
        'UserName' : 'Himanshu',
        'title' : 'post1',
        'content' : 'Job Search',
        'date' : '15-12-2000'
    },
    {
        'UserName' : 'Harshit',
        'title' : 'post2',
        'content' : 'In love with Sanju',
        'date' : '24-3-2000'
    },
    {
        'UserName' : 'Gourav',
        'title' : 'post3',
        'content' : 'How to be less busy',
        'date' : '20-10-1999'
    },
    {
        'UserName' : 'Dhaval',
        'title' : 'post4',
        'content' : 'How to be stalker',
        'date' : '24-4-2000'
    }
]

@app.route("/")
@app.route("/home")
def homePage():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/register", methods = ['GET' , 'POST'] )
def register():
    form = RegistrationForm()
    if form.validate_on_submit() :
        flash(f"Account Created for {form.userName.data}!" , "success")
        return redirect(url_for('homePage')) 
    return render_template('register.html', title = "Register", form = form)

@app.route("/login", methods = ['GET' , 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit() :
        flash(f"LogIn Successfull" , "success")
        return redirect(url_for('homePage')) 
    return render_template('login.html', title = "Login", form = form)