# event.py

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://amino:201JMT3242@cluster0.1l7tdn6.mongodb.net/users?retryWrites=true&w=majority")
db = client["users"]
collection = db["events"]

def predict_top_events():
    try:
        # Fetch data
        data = collection.find()

        # Initialize a list to store events and their likes count
        events_likes = []

        # Iterate through events to get likes count for each event
        for event in data:
            likes_count = len(event["likes"])
            events_likes.append((event["title"], likes_count))

        # Sort the events by likes count in descending order
        sorted_events = sorted(events_likes, key=lambda x: x[1], reverse=True)

        # Get the top three events
        top_three_events = sorted_events[:3]

        return top_three_events

    except Exception as e:
        return f"An error occurred: {str(e)}"
