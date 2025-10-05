ExoAI — Exoplanet Vetting Web Application

ExoAI is a lightweight web application that classifies exoplanet candidates into Confirmed or Candidate with their probabilities using an XGBoost machine learning model.  
The project integrates a Flask backend for API handling, a Tailwind CSS frontend for a minimal and responsive user interface, and a trained XGBoost model for predictions.

---

Project Overview

The purpose of this application is to demonstrate how machine learning models can be deployed as web services.  
Users can input planetary parameters or upload a dataset through a simple frontend interface, send them to the backend API, and receive model predictions in real time.

Tech Stack:
- Frontend: Tailwind CSS, HTML, JavaScript  
- Backend: Flask (Python)  
- Machine Learning: XGBoost  
- API Communication: REST (JSON)

---

How It Works

1. Frontend (Tailwind UI):
   The user interacts with a clean, minimal interface built using Tailwind. It collects planetary data and sends it to the backend API using `fetch()` or Axios.

2. Backend (Flask Server): 
   Flask handles incoming requests at defined endpoints (e.g., `/predict`). The backend loads the trained XGBoost model, processes input data, and returns a prediction as JSON.

3. Model (XGBoost):  
   The trained model evaluates the input features (such as radius, mass, orbital period, etc.) and classifies the target as a confirmed exoplanet or false positive.

4. API Response:  
   The backend sends the prediction result back to the frontend, which displays it on the web interface.
