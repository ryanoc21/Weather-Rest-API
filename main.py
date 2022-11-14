from flask import Flask, render_template
import pandas as pd

# Instantiate website object
app = Flask(__name__)

df_station = pd.read_csv("/Users/ryanoconnor/Desktop/Bootcamp_update/weather_api/data_small/stations.txt", skiprows=17)
station_table = df_station[['STAID', 'STANAME                                 ']]


# Connect the html page with the website object
@app.route("/")
def home():
    return render_template("home.html",data=station_table.to_html())


# Function to allow the users to input a specific year and date to retrieve the data
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Concatenate the user input station id to the file route
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"

    # Read the dataframe
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

# Function to display all data for a station
@app.route("/api/v1/<station>")
def all_data(station):
    # Concatenate the user input station id to the file route
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"

    # Read the dataframe
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    # Turn the data to a dictionary
    data = df.to_dict(orient="records")
    return data


app.run(debug=True)
