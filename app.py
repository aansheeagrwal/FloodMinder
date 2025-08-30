"""FloodMinder Web App."""

import flask
from flask import Flask, render_template, request
import joblib
import base64
from training import prediction
import requests
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# -------------------------
# Static city and month lists
# -------------------------
data = [
    {'name':'Delhi', "sel": "selected"},
    {'name':'Mumbai', "sel": ""},
    {'name':'Kolkata', "sel": ""},
    {'name':'Bangalore', "sel": ""},
    {'name':'Chennai', "sel": ""}
]

months = [
    {"name":"May", "sel": ""},
    {"name":"June", "sel": ""},
    {"name":"July", "sel": "selected"}
]

cities = [
    {'name':'Delhi', "sel": "selected"},
    {'name':'Mumbai', "sel": ""},
    {'name':'Kolkata', "sel": ""},
    {'name':'Bangalore', "sel": ""},
    {'name':'Chennai', "sel": ""},
    {'name':'New York', "sel": ""},
    {'name':'Los Angeles', "sel": ""},
    {'name':'London', "sel": ""},
    {'name':'Paris', "sel": ""},
    {'name':'Sydney', "sel": ""},
    {'name':'Beijing', "sel": ""}
]

# -------------------------
# Load trained model
# -------------------------
model = joblib.load("model.pickle")

# -------------------------
# Routes
# -------------------------
@app.route("/")
@app.route('/index.html')
def index() -> str:
    """Render homepage."""
    return render_template("index.html")


@app.route('/plots.html')
def plots():
    return render_template('plots.html')


@app.route('/heatmaps.html')
def heatmaps():
    return render_template('heatmaps.html')


@app.route('/satellite.html', methods=['GET', 'POST'])
def satellite():
    """Render satellite page and update image based on selection."""
    if request.method == 'POST':
        place = request.form.get('place')
        date = request.form.get('date')

        # Reset selection
        for item in data:
            item["sel"] = "selected" if item["name"] == place else ""
        for item in months:
            item["sel"] = "selected" if item["name"] == date else ""

        text = f"{place} in {date} 2020"
        direc = f"processed_satellite_images/{place}_{date}.png"
    else:
        # Default
        place = "Delhi"
        date = "July"
        text = f"{place} in {date} 2020"
        direc = "processed_satellite_images/Delhi_July.png"

    # Load image as base64
    try:
        with open(direc, "rb") as image_file:
            image = base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        image = None

    return render_template('satellite.html', data=data, image_file=image, months=months, text=text)


@app.route('/predicts.html', methods=["GET", "POST"])
def predicts():
    """Render prediction page and calculate flood prediction."""
    if request.method == "POST":
        try:
            cityname = request.form["city"]

            # Reset selection
            for item in cities:
                item['sel'] = 'selected' if item['name'] == cityname else ''

            # Get latitude and longitude from HERE API
            URL = "https://geocode.search.hereapi.com/v1/geocode"
            PARAMS = {
                'apikey':'Bwv2FJJQHT4FTQBWFC7IEKRE49lNYtrAti6NK7uJVCY',  # Replace with your API key
                'q': cityname
            }
            r = requests.get(url=URL, params=PARAMS)
            data_json = r.json()

            latitude = data_json['items'][0]['position']['lat']
            longitude = data_json['items'][0]['position']['lng']

            # Get features from prediction module
            final = prediction.get_data(latitude, longitude)
            final[4] *= 15  # Adjust precipitation

            pred = "Safe" if str(model.predict([final])[0]) == "0" else "Unsafe"

            return render_template(
                'predicts.html',
                cityname=f"Information about {cityname}",
                cities=cities,
                temp=round(final[0], 2),
                maxt=round(final[1], 2),
                wspd=round(final[2], 2),
                cloudcover=round(final[3], 2),
                percip=round(final[4], 2),
                humidity=round(final[5], 2),
                pred=pred
            )
        except Exception as e:
            print("Error:", e)
            return render_template('predicts.html', cities=cities, cityname="Oops, we weren't able to retrieve data for that city.")
    else:
        return render_template('predicts.html', cities=cities, cityname="Information about the city")


# -------------------------
# Contact Form Route
# -------------------------
@app.route('/contact', methods=['POST'])
def contact():
    """Handle AJAX contact form submission."""
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if not name or not email or not subject or not message:
            return "Please fill in all fields", 400

        # Compose email
        msg = EmailMessage()
        msg['Subject'] = f"FloodMinder Contact Form: {subject}"
        msg['From'] = email
        msg['To'] = "your_email@example.com"  # replace with your email
        msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

        # Send email via SMTP (Gmail example)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('your_email@example.com', 'your_email_password')  # use app password
            smtp.send_message(msg)

        return "OK"

    except Exception as e:
        print("Contact form error:", e)
        return f"Error sending message: {str(e)}", 500


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
