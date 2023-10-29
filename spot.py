import pymongo
import pandas as pd

# MongoDB connection information
mongodb_uri = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongodb_uri)
db = client["sai"]
collection = db["orginalphone"]

# Function to display data in a table
def display_data():
    cursor = collection.find()
    data = list(cursor)
    if data:
        df = pd.DataFrame(data)
        print(df)
    else:
        print("No data found in the collection.")

# Function to add tags to a document
def add_tags(doc_id, tags):
    collection.update_one({"_id": doc_id}, {"$set": {"tags": tags}})
    print(f"Tags added to document with _id {doc_id}.")

# Interactive menu
while True:
    print("\nOptions:")
    print("1. Display data")
    print("2. Add tags")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        display_data()
    elif choice == "2":
        doc_id = input("Enter the document _id to add tags: ")
        tags = input("Enter tags (comma-separated): ").split(',')
        add_tags(doc_id, tags)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option.")

# Close the MongoDB connection
client.close()
