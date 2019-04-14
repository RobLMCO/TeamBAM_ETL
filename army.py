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
army_file = "base_locations.csv"
army_df = pd.read_csv(army_file)

engine = create_engine("sqlite:///army_1.sqlite", echo=False)
engine.table_names()
try:
    army_df.to_sql(name='base_locations', con=engine, index=True)
except:
    pass

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
    
    
    return render_template('ALL.html', results="Results go here!")
    


@app.route("/api/v1.0/commands/FORSCOM")
def FORSCOM():
    
    return render_template('FORSCOM.html', results="Results go here!")
    

@app.route("/api/v1.0/commands/CENTCOM")
def CENTCOM():
    
    return render_template('CENTCOM.html', results="Results go here!")
    

@app.route("/api/v1.0/commands/ARNG")
def ARNG():
    
    return render_template('ARNG.html', results="Results go here!")
    

@app.route("/api/v1.0/commands/Training")
def TRNG():
    
    
    return render_template('Training.html', results="Results go here!")
   

@app.route("/api/v1.0/commands/USARPAC")
def USARPAC():
    
    
    return render_template('USARPAC.html', results="Results go here!")
    

@app.route("/api/v1.0/commands/USAREUR")
def USAREUR():
    
    
    return render_template('USAREUR.html', results="Results go here!")
    

@app.route("/api/v1.0/commands/SOF")
def SOF():
    
    
    return render_template('SOCCOM.html', results="Results go here!")
    

@app.route("/api/v1.0/commands/TRADOC")
def TRADOC():
    
    
    return render_template('TRADOC.html', results="Results go here!")
    

@app.route("/api/v1.0/regions/CONUS")
def CONUS():
    results = []
    conus_quantity = 0
    conus_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Region='CONUS'")

    for total in conus_quantity:
        print(total)
    
    conus=engine.execute("SELECT * from base_locations where Region='CONUS'")
    for result in conus:
        results.append(result)
        print(result)
    
    return render_template('CONUS.html', total=total, results=results)
    

@app.route("/api/v1.0/regions/OCONUS")
def OCONUS():
    results = []
    oconus_quantity = 0
    oconus_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Region='OCONUS'")

    for total in oconus_quantity:
        print(total)
    
    oconus=engine.execute("SELECT * from base_locations where Region='OCONUS'")
    for result in oconus:
        results.append(result)
        print(result)
    
    return render_template('OCONUS.html', total=total, results=results)
    

@app.route("/api/v1.0/types/Air")
def AIR():
    results = []
    air_rvct_quantity = 0
    air_rvct_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where type='Air RVCT'")

    for total in air_rvct_quantity:
        print(total)
    
    air_rvct=engine.execute("SELECT * from base_locations where type='Air RVCT'")

    for result in air_rvct:
        results.append(result)
        print(result)


    return render_template('AIR.html', total=total, results=results)
    
@app.route("/api/v1.0/types/Ground")
def GROUND():
    results = []
    ground_rvct_quantity = 0
    ground_rvct_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where type='Ground RVCT'")

    for total in ground_rvct_quantity:
        print(total)
    
    ground_rvct=engine.execute("SELECT * from base_locations where type='Ground RVCT'")

    for result in ground_rvct:
        results.append(result)
        print(result)
    
    return render_template('GROUND.html', total=total, results=results)
    

@app.route("/api/v1.0/report")
def report():
    
    
    return render_template('REPORT.html')
    #return jsonify(base_locations_dict)

if __name__ == '__main__':
    app.run(debug=True)
