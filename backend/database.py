# To use database:
# pip install pymongo

from pymongo import MongoClient

import fastapi2

connection_string = "mongodb+srv://no89:<8pzd1hFpG5KFqPCK>@mydatabase.x3ahw.mongodb.net/?retryWrites=true&w=majority&appName=mydatabase"

# Connect to MongoDB Atlas
client = MongoClient(connection_string)

# Specify the database and collection
db = client["my_database"]
collection = db["users"]

# Get user input
name = input("Enter your name: ")
email = input("Enter your email: ")
resume = response

# Create a document to insert into MongoDB
user_data = {
    "name": name,
    "email": email,
    "resume": resume
}

# Insert the document into the collection
collection.insert_one(user_data)

print("Data successfully inserted!")

# Close the connection
client.close()