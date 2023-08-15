# Import the dependencies.
# Module 10 - Day 3 - Activity 6,10, Office hours

from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd
import datetime as dt
from datetime import timedelta

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()

# reflect the tables
base.prepare(autoload_with=engine)

# Save references to each table
station = base.classes.station
measurement = base.classes.measurement

# Create our session (link) from Python to the DB
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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Convert the most recent date from string to a Python date object
    recent_date = session.query(func.max(measurement.date)).scalar()
    recent_date = dt.datetime.strptime(recent_date, "%Y-%m-%d").date()
    past_year = recent_date - dt.timedelta(days = 365)
    
    data = session.query(measurement.date, measurement.prcp).filter(measurement.date >= past_year).all()

    precipitation_data =  {date: prcp for date, prcp in data}
    
    # Return the precipitation data as a JSON 
    return jsonify(precipitation_data)

@app.route('/api/v1.0/stations')
def stations():
    stations = session.query(station.station).distinct().all()

    station_data = [row.station for row in stations]
 
    return jsonify(station_data)

@app.route('/api/v1.0/tobs')
def active_station():

    active_station = session.query(func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)).filter(measurement.station == 'USC00519281').order_by(func.min(measurement.tobs)).all()
    
    recent_date = session.query(func.max(measurement.date)).filter(measurement.station == active_station.station)
    recent_date = dt.datetime.strptime(recent_date, "%Y-%m-%d").date()
    
    past_year = recent_date - timedelta(days = 365)
    
    data = session.query(measurement.tobs).filter(measurement.station == active_station.station,measurement.date >= past_year,measurement.date <= recent_date).all()
    
    active_station_data = [row.tobs for row in data]

    return jsonify(active_station_data)

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temperature(start=None, end=None):
    
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date() if end else None
    
    if end_date:
        results = session.query(
            func.min(measurement.tobs).label('TMIN'),
            func.avg(measurement.tobs).label('TAVG'),
            func.max(measurement.tobs).label('TMAX')
        ).filter(
            measurement.date >= start_date,
            measurement.date <= end_date
        ).all()
    else:
        results = session.query(
            func.min(measurement.tobs).label('TMIN'),
            func.avg(measurement.tobs).label('TAVG'),
            func.max(measurement.tobs).label('TMAX')
        ).filter(
            measurement.date >= start_date
        ).all()

if __name__ == "__main__":
    app.run(debug=False)
    
session.close()
