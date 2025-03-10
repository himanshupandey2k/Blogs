from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'eef620ea683b020344456048dfa82a'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = "Login", form = form)