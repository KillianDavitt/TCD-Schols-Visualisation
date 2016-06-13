#!/usr/bin/python3
import flask
import flask_sqlalchemy
import shutil
from flask import render_template

HOST = "0.0.0.0"
PORT = 80
DEBUG=True

# Setup the flask app, db and token.
app = flask.Flask(__name__, static_url_path='/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scholars.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = flask_sqlalchemy.SQLAlchemy(app)
db.create_all()

##########
# Models #
##########

class Scholar(db.Model):
  scholar_id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String())
  course = db.Column(db.String())
  year = db.Column(db.Integer)

  def __init__(self, name, course, year):
    self.id = id
    self.path = path
    self.filename = filename

##########
# Routes #
##########

# list all files.
@app.route("/", methods=["GET"])
def list_files():
  yearly_totals = []

  year = 1990
  while(year<=2016):
    year_tot = Scholar.query.filter_by(year=year).all()
    yearly_totals.append(len(year_tot))
    year += 1
 
  
  return render_template('index.html', yearly_totals=yearly_totals)

@app.route('/turret.min.css/hi/hi')
def turret():
  print("IONN")
  return app.send_static_file('turret.min.css')

#######
# Run #
#######

if __name__ == "__main__":
  db.create_all()
  app.run(host=HOST, port=PORT, debug=DEBUG)
