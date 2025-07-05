import pymongo
import csv
import random
from datetime import datetime, timedelta

# Replace with your Atlas connection string
connection_string = mongodb+srv://sinharudra60:Bukballa@66@cluster-rudra-01.biwb90c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Rudra-01

# Connect to MongoDB Atlas
client = pymongo.MongoClient(connection_string)

# Create/select database and collection
db = client["music_db"]
collection = db["streaming_events"]

# Clear the collection (optional)
collection.delete_many({})

# Generate synthetic timestamps
base_timestamp = datetime(2025, 5, 17, 10, 0, 0)  # Base timestamp: May 17, 2025, 10:00 AM

# Read and parse the modified CSV
streaming_records = []
with open("streaming_data_modified.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Generate synthetic timestamp
        random_minutes = random.randint(0, 1440)  # Random timestamp within 24 hours
        listen_timestamp = (base_timestamp + timedelta(minutes=random_minutes)).isoformat() + "Z"

        # Transform the row into a MongoDB document
        record = {
            "user_id": row["user_id"],
            "artist": row["Artist"],
            "genre": row["genre"],
            "listen_timestamp": listen_timestamp,
            "title": row["Title"],
            "year": int(row["Year"]),
            "sales": int(row["Sales"]),
            "streams": int(row["Streams"]),
            "downloads": int(row["Downloads"]),
            "radio_plays": int(row["Radio Plays"]),
            "rating": float(row["Rating"])
        }
        streaming_records.append(record)

# Insert records into MongoDB
collection.insert_many(streaming_records)

# Verify the insertion
print(f"Inserted {collection.count_documents({})} records.")
for record in collection.find().limit(5):
    print(record)

# Close the connection
client.close()