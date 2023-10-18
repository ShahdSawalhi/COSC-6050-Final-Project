"""
This is the python file to start developing a data analytics tool that looks into crime data of a specific location.
The app.py file will include all routes to the different pages within the website being developed.
Each page will have an HTML/CSS file to deal with the style and content of the page.
"""

# Import all libraries needed
from flask import Flask, render_template
import csv
import pandas as pd
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Load data from the CSV file into a Pandas DataFrame
data = pd.read_csv('wibr.csv')

# Rename the columns to match the template
data.rename(columns={'RoughX': 'latitude', 'RoughY': 'longitude'}, inplace=True)

# Convert DataFrame to a list of dictionaries
crime_data = data.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('layout.html')  # Render the index.html template

@app.route('/crime_map')
def crime_map():
    return render_template('crime_map.html', crime_data=crime_data)  # Render the crime_map.html template

@app.route('/predictive_policing')
def predictive_policing():
    # Implement predictive policing logic here
    return render_template('predictive_policing.html')  # Render the predictive_policing.html template

if __name__ == '__main__':
    app.run(port=5050, debug=True)

#Testing PyCharm push-pull -Patricia