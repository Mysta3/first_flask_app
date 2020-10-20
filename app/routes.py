from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/sample_form')
def sample_form():
    return render_template("form.html")


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


@app.route('/post_data', methods=['POST'])
def post_data():
    if request.method == "POST":
        first_name = str(request.form['first_name'])
        last_name = str(request.form['last_name'])
        print(f'{first_name} " : "{last_name}')
    return redirect("http://127.0.0.1:5000/thanks", code=302)
