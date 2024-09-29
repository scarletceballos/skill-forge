# To use database:
# pip install pymongo

#Only function of this class is to take response.json and store in a MongoDB database.
from pymongo import MongoClient

import fastapi2

class DBCOnnection:
    def __init__(self):
        # Connect to MongoDB Atlas
        # Specify the database and collection
        self.connection_string = "mongodb+srv://no89:<8pzd1hFpG5KFqPCK>@mydatabase.x3ahw.mongodb.net/?retryWrites=true&w=majority&appName=mydatabase"
        self.db = self.client("my_database")
        self.collection  = self.db["users"]
    

    def insert_a_user(response):
        #resposne is sent from fastapi when it makes a call
        resume = response
        user_data = {
            "name": resume.name,
            "email": resume.email,
            "resume text": resume.text
            collection.insert_one(user_data)
            print("Data successfully inserted!")
            client.close()
        }

    def close(self):
        self.client.close()




