from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

# load home page
@app.route("/")
def index():
    return render_template('index.html')


# load welcome page with username
@app.route("/welcome", methods=['GET','POST'])
def welcome():
    username = request.form['username']
    usernameError = ""

    if " " in username:
        usernameError = "That's not a valid username"
        return render_template ("index.html", username=username, usernameError=usernameError)
    else:
        return render_template("welcome.html", username=username)

app.run()