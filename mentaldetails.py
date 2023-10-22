import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)

# MongoDB connection information
mongodb_uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongodb_uri)
db = client["sai"]
collection = db["orginalphone"]

# Function to fetch and display data
def get_data():
    cursor = collection.find()
    data = list(cursor)
    return data

# Function to add tags to a document
def add_tags(doc_id, tags):
    collection.update_one({"_id": doc_id}, {"$set": {"tags": tags}})

# Route for the main page
@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

# Route for adding tags
@app.route('/add_tags', methods=['POST'])
def add_tags_route():
    doc_id = request.form['doc_id']
    tags = request.form['tags'].split(',')
    add_tags(doc_id, tags)
    return "Tags added successfully."

if __name__ == '__main__':
    app.run(debug=True)
