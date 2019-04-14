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
    results = []
    all_quantity = 0
    
    all_quantity=engine.execute("SELECT SUM(Quantity) from base_locations")

    for total in all_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    all=engine.execute("SELECT * from base_locations")

    for result in all:
        results.append(result)
        print(result)
    
    return render_template('ALL.html', total=total, results=results)
    


@app.route("/api/v1.0/commands/FORSCOM")
def FORSCOM():
    results = []
    forscom_quantity = 0
    
    forscom_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='FORSCOM'")

    for total in forscom_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    forscom=engine.execute("SELECT * from base_locations where Command='FORSCOM'")

    for result in forscom:
        results.append(result)
        print(result)


    return render_template('FORSCOM.html', total=total, results=results)
    

@app.route("/api/v1.0/commands/CENTCOM")
def CENTCOM():
    results = []
    centcom_quantity = 0
    
    centcom_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='CENTCOM'")

    for total in centcom_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    centcom=engine.execute("SELECT * from base_locations where Command='CENTCOM'")

    for result in centcom:
        results.append(result)
        print(result)

    return render_template('CENTCOM.html', total=total, results=results)
    

@app.route("/api/v1.0/commands/ARNG")
def ARNG():
    results = []
    arng_quantity = 0
    
    arng_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='ARNG'")

    for total in arng_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    arng=engine.execute("SELECT * from base_locations where Command='ARNG'")

    for result in arng:
        results.append(result)
        print(result)

    return render_template('ARNG.html', total=total, results=results)
    

@app.route("/api/v1.0/commands/Training")
def TRNG():
    results = []
    training_quantity = 0
    
    training_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='Training'")

    for total in training_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    training=engine.execute("SELECT * from base_locations where Command='Training'")

    for result in training:
        results.append(result)
        print(result)
    
    return render_template('Training.html', total=total, results=results)
   

@app.route("/api/v1.0/commands/USARPAC")
def USARPAC():
    results = []
    usarpac_quantity = 0
    
    usarpac_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='USARPAC'")

    for total in usarpac_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    usarpac=engine.execute("SELECT * from base_locations where Command='USARPAC'")

    for result in usarpac:
        results.append(result)
        print(result)
    
    return render_template('USARPAC.html', total=total, results=results)
    

@app.route("/api/v1.0/commands/USAREUR")
def USAREUR():
    results = []
    usareur_quantity = 0
    
    usareur_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='USAREUR'")

    for total in usareur_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    usareur=engine.execute("SELECT * from base_locations where Command='USAREUR'")

    for result in usareur:
        results.append(result)
        print(result)
    
    return render_template('USAREUR.html', total=total, results=results)
    

@app.route("/api/v1.0/commands/SOF")
def SOF():
    results = []
    soccom_quantity = 0
    
    soccom_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='SOF'")

    for total in soccom_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    soccom=engine.execute("SELECT * from base_locations where Command='SOF'")

    for result in soccom:
        results.append(result)
        print(result)
    
    return render_template('SOCCOM.html', total=total, results=results)
    

@app.route("/api/v1.0/commands/TRADOC")
def TRADOC():
    results = []
    tradoc_quantity = 0
    
    tradoc_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Command='TRADOC'")

    for total in tradoc_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
        print(total)

    tradoc=engine.execute("SELECT * from base_locations where Command='TRADOC'")

    for result in tradoc:
        results.append(result)
        print(result)
    
    return render_template('TRADOC.html', total=total, results=results)
    

@app.route("/api/v1.0/regions/CONUS")
def CONUS():
    results = []
    conus_quantity = 0
    conus_quantity=engine.execute("SELECT SUM(Quantity) from base_locations where Region='CONUS'")

    for total in conus_quantity:
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
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
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
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
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
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
        total = str(total)
        total = total.replace("(", "")
        total = total.replace(")", "")
        total = total.replace(",", "")
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
