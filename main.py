from flask import Flask, render_template, request
from flask_frozen import Freezer


app = Flask(__name__)



@app.route('/')
def index():
	return render_template('index.html')


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()