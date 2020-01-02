from flask import Flask, escape, request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/gsm_new'
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return render_template('home/index.html')


if __name__ == '__main__':
	app.run(debug=True)