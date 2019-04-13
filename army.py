import numpy as np
import pandas as pd

import datetime as dt
from dateutil import parser

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/army.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/all<br/>"
        f"/api/v1.0/commands/FORSCOM<br/>"
        f"/api/v1.0/commands/ARNG<br/>"
        f"/api/v1.0/commands/Training<br/>"
        f"/api/v1.0/commands/USARPAC<br/>"
        f"/api/v1.0/commands/USAREUR<br/>"
        f"/api/v1.0/commands/SOF<br/>"
        f"/api/v1.0/regions<br/>"
        f"/api/v1.0/types<br/>"
        f"/api/v1.0/report<br/>"
    )


@app.route("/api/v1.0/all")
def all():
    
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    precipitation_df=pd.DataFrame(precipitation_data)
    precipitation_dict = precipitation_df.to_dict()

    return jsonify(precipitation_dict)


@app.route("/api/v1.0/commands/FORSCOM")
def FORSCOM():
    stations_data = session.query(Measurement.station).all()
    
    return jsonify(stations_data)

@app.route("/api/v1.0/commands/ARNG")
def ARNG():
    
    temperature_data = session.query(Measurement.station,Measurement.date, Measurement.tobs).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    temperatures_df=pd.DataFrame(temperature_data)
    temperatures_dict = temperatures_df.to_dict()
    return jsonify(temperatures_dict)

@app.route("/api/v1.0/commands/Training")
def start(start):
    start_date = start
    startdate_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    return jsonify(startdate_data)

@app.route("/api/v1.0/commands/USARPAC")
def startend(start,end):
    start_date = start
    end_date = end
    startenddates_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    return jsonify(startenddates_data)

@app.route("/api/v1.0/commands/USAREUR")
def start(start):
    start_date = start
    startdate_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    return jsonify(startdate_data)

@app.route("/api/v1.0/commands/SOF")
def startend(start,end):
    start_date = start
    end_date = end
    startenddates_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    return jsonify(startenddates_data)

@app.route("/api/v1.0/regions")
def regions():
    
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    precipitation_df=pd.DataFrame(precipitation_data)
    precipitation_dict = precipitation_df.to_dict()

    return jsonify(precipitation_dict)

@app.route("/api/v1.0/types")
def types():
    
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    precipitation_df=pd.DataFrame(precipitation_data)
    precipitation_dict = precipitation_df.to_dict()

    return jsonify(precipitation_dict)

@app.route("/api/v1.0/report")
def report():
    
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date > last_year).\
    order_by(Measurement.date).all()
    precipitation_df=pd.DataFrame(precipitation_data)
    precipitation_dict = precipitation_df.to_dict()

    return jsonify(precipitation_dict)

if __name__ == '__main__':
    app.run(debug=True)
