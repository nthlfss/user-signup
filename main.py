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
    
    # get inputs from form
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    # set errors to empty
    usernameError = ""
    passwordError = ""
    verifyError = ""
    emailError = ""

    # verify inputs
    if " " in username or len(username) < 3 or len(username) > 20:
        usernameError = "That's not a valid username"
    if len(password) < 3 or len(password) > 20:
        passwordError = "That's not a valid password"
    if verify != password:
        verifyError = "Passwords don't match"
    if " " in email or len(email) < 3 or len(email) > 20 or "." not in email or "@" not in email:
        emailError = "That's not a valid email"

    # if all errors are empty, got to welcome page
    if not usernameError and not passwordError and not verifyError and not emailError:
        return render_template("welcome.html", username=username)
    # else reload index with error messages
    else:
        return render_template ("index.html", username=username, usernameError=usernameError, passwordError=passwordError, verifyError=verifyError, email=email, emailError=emailError)

app.run()