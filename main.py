from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/add", methods=['POST'])
def add_info():
    username = request.form['username']
    password = request.form['password']

    return render_template('welcome.html', username=username)


@app.route("/")
def index():
    return render_template('index.html')

app.run()