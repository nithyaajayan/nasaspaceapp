from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("xgb_planet_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    probability = None
    if request.method == "POST":
        try:
            # Extract parameters from form
            params = [
                float(request.form["orb_period"]),
                float(request.form["tran_dur"]),
                float(request.form["tran_depth"]),
                float(request.form["planet_radius"]),
                float(request.form["eq_temp"]),
                float(request.form["insol_flux"]),
                float(request.form["stellar_teff"]),
                float(request.form["stellar_logg"]),
                float(request.form["stellar_rad"]),
                float(request.form["ra"]),
                float(request.form["dec"]),
            ]
            
            # Convert to array for prediction
            input_array = np.array([params])
            
            # Predict
            result = model.predict(input_array)[0]
            probability = model.predict_proba(input_array)[0][1]  # Probability of class 1
            
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
