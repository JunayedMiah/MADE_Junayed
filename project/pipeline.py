import requests
import pandas as pd
import sqlite3
import os


url1 = "https://data.montgomerycountymd.gov/api/views/mmzv-x632/rows.csv?accessType=DOWNLOAD"
url2 = "https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv?accessType=DOWNLOAD"
    


# Function to load and clean the data for the crash reporting dataset
def clean_crash_reporting_data():
    df1 = pd.read_csv('data/crash_reporting.csv')

    # Keep only the specified columns from df1
    crash_reporting_columns = ['Crash Date/Time', 'Route Type', 'Road Name', 'Collision Type', 'Weather', 'Surface Condition',
                               'Light', 'Traffic Control', 'Driver At Fault', 'Speed Limit', 'Driverless Vehicle',
                               'Vehicle Model', 'Latitude', 'Longitude']
    df1 = df1[crash_reporting_columns]

    # Drop rows with missing values in all columns
    df1.dropna(how='any', inplace=True)

    # Clean column names: remove spaces and lowercase them
    df1.columns = df1.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Conntect to Sqlite database
    conn = sqlite3.connect('data/.crash_reporting.db')
    df1.to_sql('crash_reporting', conn, if_exists='replace', index=False)

    print("Crash Reporting data cleaned and saved successfully!")
    return df1

# Function to load and clean the vehicle collision dataset
def clean_vehicle_collision_data():
    df2 = pd.read_csv('data/vehicle_collision.csv')

    # Keep only the specified columns from df2
    vehicle_collision_columns = ['CRASH DATE', 'CRASH TIME', 'BOROUGH', 'LATITUDE', 'LONGITUDE', 'ON STREET NAME', 
                                 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED', 'VEHICLE TYPE CODE 1']
    df2 = df2[vehicle_collision_columns]

    # Drop rows with missing values in all columns
    df2.dropna(how='any', inplace=True)

    # Clean column names: remove spaces and lowercase them
    df2.columns = df2.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # connect to SQlite database
    conn = sqlite3.connect('data/.vehicle_collision.db')
    df2.to_sql('vehicle_collision', conn, if_exists='replace', index=False)

    print("Vehicle Collision data cleaned and saved successfully!")
    return df2

# Main function to run the entire pipeline
def run_pipeline():

    # Step 2: Clean and transform data
    clean_crash_reporting_data()
    clean_vehicle_collision_data()

if __name__ == "__main__":
    run_pipeline()
