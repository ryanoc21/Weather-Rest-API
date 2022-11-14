from flask import Flask, render_template
import pandas as pd

# Instantiate website object
app = Flask(__name__)


# Connect the html page with the website object
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Concatenate the user input station id to the file route
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"

    # Read the dataframe
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}


app.run(debug=True)
