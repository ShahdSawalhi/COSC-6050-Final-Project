"""
This is the python file to start developing a data analytics tool that looks into crime data of a specific location.
The app.py file will include all routes to the different pages within the website being developed.
Each page will have an HTML/CSS file to deal with the style and content of the page.
"""

# Import all libraries needed
from flask import Flask, render_template, request
import csv
import pandas as pd




app = Flask(__name__, template_folder="templates" , static_folder="Static")
# Load data from the CSV file into a Pandas DataFrame
data = pd.read_csv('wibr.csv')
# Rename the columns to match the template
data.rename(columns={'RoughX': 'latitude', 'RoughY': 'longitude'}, inplace=True)
# Convert DataFrame to a list of dictionaries
crime_data = data.to_dict(orient='records')

#Define Functions below
def fetch_crime_frequency_data():
    data = pd.read_csv('wibr.csv')

    # Update the column names
    crime_type_columns = ['Arson', 'Assault', 'Burglary', 'CriminalDamage', 'Homicide', 'Robbery', 'SexOffense', 'Theft', 'VehicleTheft']

    # Calculate the frequency of each crime type
    crime_frequency = data[crime_type_columns].sum().reset_index()
    crime_frequency.columns = ['Crime_Type', 'Frequency']

    # Convert the result to a list of dictionaries
    crime_frequency_data = crime_frequency.to_dict(orient='records')

    return crime_frequency_data

def fetch_crime_type_data():
    data = pd.read_csv('wibr.csv')

    # Update the column names
    crime_type_columns = ['Arson', 'Assault', 'Burglary', 'CriminalDamage', 'Homicide', 'Robbery', 'SexOffense', 'Theft', 'VehicleTheft']

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
    return render_template('crime_map.html')  # Render the crime_map.html template


@app.route('/predictive_policing', methods=['GET', 'POST'])
def predictive_policing():
    # Fetch crime frequency data
    crime_frequency_data = fetch_crime_frequency_data()

    # Fetch crime type statistics
    crime_type_statistics = fetch_crime_type_data()

    # Combine both datasets into a single dictionary
    crime_data = {crime['Crime_Type']: {'Total': crime['Frequency']} for crime in crime_frequency_data}

    if request.method == 'POST':
        selected_crime_type = request.form.get('crime_type_filter')
        selected_crime_data = {selected_crime_type: crime_type_statistics.get(selected_crime_type, {})}
        return render_template('predictive_policing.html', statistic_data=selected_crime_data)

    # Render the initial page with all crime data
    return render_template('predictive_policing.html', statistic_data=crime_data)




@app.route('/resources')
def resources():
    return render_template('resources.html')


if __name__ == '__main__':
    app.run(port=5050, debug=True)


##Testing 2-PM