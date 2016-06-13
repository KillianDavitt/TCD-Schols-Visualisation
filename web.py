#!/usr/bin/python3
import flask
import flask_sqlalchemy
import shutil
from flask import render_template

HOST = "127.0.0.1"
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
 
 
  

  query = db.session.query(Scholar.course.distinct().label("course"))
  courses = [row.course for row in query.all()]

  course_data = []

  for item in courses:
    test_total = Scholar.query.filter_by(course=item).all()
    if len(test_total) <30:
        continue
    yearly_total_course = []
    year = 1990
    while(year<=2016):
      year_tot = Scholar.query.filter_by(year=year, course=item).all()
      yearly_total_course.append(len(year_tot))
      year += 1
 
    thing = (item, yearly_total_course)

    course_data.append(thing)


  return render_template('index.html', yearly_totals=yearly_totals, course_data=course_data[:10])

#######
# Run #
#######

if __name__ == "__main__":
  db.create_all()
  app.run(host=HOST, port=PORT, debug=DEBUG)
