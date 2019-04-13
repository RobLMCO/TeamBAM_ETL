import numpy as np
import pandas as pd

import datetime as dt
from dateutil import parser

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///Resources/army.sqlite?check_same_thread=False")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
#Measurement = Base.classes.measurement
#Station = Base.classes.station

session = Session(engine)

base_locations_dict = {'name:', 'chicken'}

#################################################
# Flask Setup
#################################################
app = Flask('flaskwp1')


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    
    return render_template('index.html')

@app.route("/api/v1.0")
def api():
    """List all available api routes."""
    return (
        f"API Instructions<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/all<br/>"
        f"/api/v1.0/commands/FORSCOM<br/>"
        f"/api/v1.0/commands/ARNG<br/>"
        f"/api/v1.0/commands/Training<br/>"
        f"/api/v1.0/commands/USARPAC<br/>"
        f"/api/v1.0/commands/USAREUR<br/>"
        f"/api/v1.0/commands/SOF<br/>"
        f"/api/v1.0/regions/CONUS<br/>"
        f"/api/v1.0/regions/OCONUS<br/>"
        f"/api/v1.0/types/Air<br/>"
        f"/api/v1.0/types/Ground<br/>"
        f"/api/v1.0/report<br/>"
    )
    

@app.route("/api/v1.0/all")
def all():
    
    #tableName = 'someTable'
    #engine = sqlalchemy.create_engine('connectionString')
    #Session = scoped_session(sessionmaker(bind=engine))
    #currentSession = Session()
    #query = 'IF ('
                      # 'EXISTS ('
                      # 'SELECT * FROM INFORMATION_SCHEMA.TABLES '
                      # 'WHERE TABLE_SCHEMA = \'dbo\' '
                      # 'AND TABLE_NAME = \'%s\')) '
                      # 'BEGIN '
                      # 'DELETE FROM [database].[dbo].[%s] '
                      # 'END' % (tableName,tableName)
    #session.execute(query)
    #print(query)
    return render_template('ALL.html', results="Results go here!")
    #return jsonify(base_locations_dict)


@app.route("/api/v1.0/commands/FORSCOM")
def FORSCOM():
    #stations_data = session.query(Measurement.station).all()
    return render_template('FORSCOM.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/CENTCOM")
def CENTCOM():
    #stations_data = session.query(Measurement.station).all()
    return render_template('CENTCOM.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/ARNG")
def ARNG():
    
    return render_template('ARNG.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/Training")
def TRNG():
    
    #startdate_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    #    filter(Measurement.date >= start_date).all()
    return render_template('Training.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/USARPAC")
def USARPAC():
    
    #startenddates_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    #    filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    return render_template('USARPAC.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/USAREUR")
def USAREUR():
    
    #startdate_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    #    filter(Measurement.date >= start_date).all()
    return render_template('USAREUR.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/SOF")
def SOF():
    
    #startenddates_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    #    filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    return render_template('SOCCOM.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/commands/TRADOC")
def TRADOC():
    
    #startenddates_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    #    filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    return render_template('TRADOC.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/regions/CONUS")
def CONUS():
    
    return render_template('CONUS.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/regions/OCONUS")
def OCONUS():
    
    return render_template('OCONUS.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/types/Air")
def AIR():
    
    
    return render_template('AIR.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/types/Ground")
def GROUND():
    
    
    return render_template('GROUND.html', results="Results go here!")
    #return jsonify(base_locations_dict)

@app.route("/api/v1.0/report")
def report():
    
    
    return render_template('REPORT.htm')
    #return jsonify(base_locations_dict)

if __name__ == '__main__':
    app.run(debug=True)
