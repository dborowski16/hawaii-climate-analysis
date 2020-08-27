import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)


# Creating Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"To get the precipitation by date: /api/v1.0/precipitation<br/>"
        f"To get a list of stations: /api/v1.0/stations<br/>"
        f"To get the observed temperature for the last 12 mos: /api/v1.0/tobs<br/>"
        f"To get min, avg, and max temp for a given start date: /api/v1.0/yyyy-mm-dd<br/>"
        f"To get min, avg, and max temp for a given date range: /api/v1.0/yyyy-mm-dd/yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['precipitation'] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    results = session.query(Measurement.station, Station.name).distinct().\
        filter(Measurement.station == Station.station).all()

    session.close()

    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    latest = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_12 = (dt.datetime.strptime(latest[0],'%Y-%m-%d') - dt.timedelta(days=365)).strftime('%Y-%m-%d')

    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= last_12).all()

    session.close()

    last_year_tobs = list(np.ravel(results))

    return jsonify(last_year_tobs)

@app.route("/api/v1.0/<start_date>")
def temp_by_start_date(start_date):
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

    session.close()

    temp_by_start_date = []
    for min, avg, max in results:
        temp_by_start_dic = {}
        temp_by_start_dic['TMIN'] = min
        temp_by_start_dic['TAVE'] = avg
        temp_by_start_dic['TMAX'] = max
        temp_by_start_date.append(temp_by_start_dic)

    return jsonify(temp_by_start_date)

@app.route("/api/v1.0/<start_date>/<end_date>")
def temp_by_date_range(start_date, end_date):
    session = Session(engine)

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    temp_by_date_range = []
    for min, avg, max in results:
        temp_by_range_dic = {}
        temp_by_range_dic['TMIN'] = min
        temp_by_range_dic['TAVE'] = avg
        temp_by_range_dic['TMAX'] = max
        temp_by_date_range.append(temp_by_range_dic)

    return jsonify(temp_by_date_range)

if __name__ == '__main__':
    app.run(debug=True)