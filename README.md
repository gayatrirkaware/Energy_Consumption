# Energy_Consumption


This project is a Flask-based web application that allows users to register, log in, and predict energy consumption based on building-related inputs. JWT (JSON Web Tokens) is used for secure user authentication. The application also stores predictions in a database for future reference.

## 🔧 Features

- User Registration
- User Login with JWT Authentication
- Password Reset (Forgot Password)
- Energy Consumption Prediction Form
- Dynamic Dropdowns for Building Type and Day of Week
- Beautiful UI with Background Images
- MongoDB Integration for User and Prediction Data

## 🚀 Tech Stack

- Python (Flask)
- HTML, CSS, JavaScript
- MongoDB
- JWT for secure authentication
- Fetch API for dynamic interactions

## 📁 Folder Structure

```

project-root/
│
├── static/
│   └── download.webp              # Background image for all pages
│
├── templates/
│   ├── login.html                 # Login page
│   ├── register.html              # User registration page
│   ├── forgot.html                # Password reset page
│   └── prediction.html            # Prediction input form
│
├── project\_app/
│   ├── **init**.py
│   ├── database.py                # MongoDB connection
│   ├── utils.py                   # Prediction logic and helpers
│
├── project\_config.py              # Configuration file with FLASK\_PORT\_NUMBER
├── app.py                         # Main Flask app with routes and JWT logic
└── README.md                      # This file

````

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/energy-consumption-prediction.git
   cd energy-consumption-prediction
````

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up your MongoDB database**

   * Create two collections:

     * `users` for storing user data
     * `testing_data` for storing predictions
   * Update the MongoDB URI and collection logic in `database.py` if needed.

4. **Add static files**

   * Place your background image at `static/download.webp`.

5. **Run the app**

   ```bash
   python app.py
   ```

   The app will run at `http://localhost:<FLASK_PORT_NUMBER>`.

## 🧪 Testing

* Register a new user at `register.html`.
* Log in at `login.html` and you'll be redirected to the prediction page on success.
* Submit prediction data to get energy usage predictions.

## 🔐 Security Note

* Change `JWT_SECRET_KEY` in `app.py` before deploying.
* Use HTTPS in production for secure token handling.

