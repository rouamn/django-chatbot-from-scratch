from django.http import JsonResponse
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://amino:201JMT3242@cluster0.1l7tdn6.mongodb.net/users?retryWrites=true&w=majority")
db = client["users"]
collection = db["events"]

def predict_top_events(request):
    try:
        # Fetch data
        data = collection.find()

        # Sort events based on likes count
        sorted_events = sorted(data, key=lambda x: len(x["likes"]), reverse=True)

        # Take the top three events
        top_three_events = sorted_events[:3]

        # Extract event details for the top three events
        result = []
        for event in top_three_events:
            event_details = {
                "title": event["title"],
                "likes": len(event["likes"]),
                "image": event.get("image", ""),  # Get image URL if available
                "date": event.get("date", ""),  # Get date if available
                "location": event.get("location", ""),  # Get location if available
                "tags": event.get("tags", [])  # Get tags if available
            }
            result.append(event_details)

        return JsonResponse(result, safe=False)  # Return JSON response

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
