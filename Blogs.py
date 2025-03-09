from flask import Flask, render_template
app = Flask(__name__)

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
        'content' : 'Searching for love',
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
        'content' : 'How to prevent stalker',
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
