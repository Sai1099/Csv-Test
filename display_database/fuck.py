from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017")  # Update with your MongoDB connection string
db = client["sai"]
collection = db["orginalphone"]

@app.route('/')
def dashboard():
    data = list(collection.find())  # Fetch all data from MongoDB collection

    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
