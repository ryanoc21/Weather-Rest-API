from flask import Flask, render_template

# Instantiate website object
app = Flask(__name__)


# Connect the html page with the website object
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "main":
    app.run(debug=True)
