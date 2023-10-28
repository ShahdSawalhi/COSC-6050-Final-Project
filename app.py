"""
This is the python file to start developing a data analytics tool that looks into crime data of a specific location.
The app.py file will include all routes to the different pages within the website being developed.
Each page will have an HTML/CSS file to deal with the style and content of the page.
"""

# Import all libraries needed
from flask import Flask, render_template, request
import csv
import pandas as pd
from geopy.geocoders import Nominatim
app = Flask(__name__, template_folder="templates")
# Load data from the CSV file into a Pandas DataFrame
data = pd.read_csv('wibr.csv')
# Rename the columns to match the template
data.rename(columns={'RoughX': 'latitude', 'RoughY': 'longitude'}, inplace=True)
# Convert DataFrame to a list of dictionaries
crime_data = data.to_dict(orient='records')

#Define Functions below
def fetch_crime_frequency_data():
    data = pd.read_csv('wibr.csv')

    # Create a list of columns that represent different crime types
    crime_type_columns = ["Arson", "AssaultOffense", "Burglary", "CriminalDamage",
                          "Homicide", "LockedVehicle", "Robbery", "SexOffense",
                          "Theft", "VehicleTheft"]

    # Calculate the frequency of each crime type
    crime_frequency = data[crime_type_columns].sum().reset_index()
    crime_frequency.columns = ['Crime_Type', 'Frequency']

    # Convert the result to a list of dictionaries
    crime_frequency_data = crime_frequency.to_dict(orient='records')

    return crime_frequency_data

def fetch_crime_type_data():
    data = pd.read_csv('wibr.csv')

    # Create a list of columns that represent different crime types
    crime_type_columns = ["Arson", "AssaultOffense", "Burglary", "CriminalDamage",
                          "Homicide", "LockedVehicle", "Robbery", "SexOffense",
                          "Theft", "VehicleTheft"]

    # Create an empty dictionary to store statistics for each crime type
    crime_type_statistics = {}

    # Calculate statistics for each crime type
    for crime_type in crime_type_columns:
        crime_type_statistics[crime_type] = {
            "Total": data[crime_type].sum(),
            "Max": data[crime_type].max(),
            "Min": data[crime_type].min(),
            "Mean": data[crime_type].mean()
        }

    return crime_type_statistics

@app.route('/')
def index():
    return render_template('layout.html')  # Render the index.html template
@app.route('/crime_map')
def crime_map():
    return render_template('crime_map.html', crime_data=crime_data)  # Render the crime_map.html template


@app.route('/predictive_policing', methods=['GET', 'POST'])
def predictive_policing():
    selected_statistic = request.form.get('selected_statistic')
    statistic_data = None  # Default value

    # Implement logic to fetch the selected statistic from the 'wibr.csv' dataset
    if selected_statistic == 'crime_type':
        # Fetch and process data for crime types
        statistic_data = fetch_crime_type_data()
    elif selected_statistic == 'crime_frequency':
        # Fetch and process data for crime frequency
        statistic_data = fetch_crime_frequency_data()
    #else:
        # Handle other statistic options
        # You can add logic here to handle other options or provide a default response

    # Ensure you return a valid response in all cases
    return render_template('predictive_policing.html', statistic_data=statistic_data)

@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(port=5050, debug=True)

    # Testing PyCharm push-pull -Patricia