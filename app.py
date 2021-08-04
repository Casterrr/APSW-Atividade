from flask import Flask, render_template

TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def index():
    return render_template('index.html')

#app.run(host='0.0.0.0', port=5000)
