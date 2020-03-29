from flask import Flask, render_template, request


app = Flask(__name__)


a=["qweqweqweqweqwe", "12654987"]
@app.route('/')
def index():
	return render_template('index.html', a=a)




app.run()
