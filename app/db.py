#this module defined interactions with the mongodb database 
#its better to make all functions execute synchronously
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://2SEProjectDatabase:ThisIsThePassword123@cluster0.21yazmx.mongodb.net/")
databaseclient = client["Cluster0"]
database = databaseclient['events']
def get_all_events():
    return list(database.find({}))
    #return an array of all events in the database 
def search_event_type(type, category):
    if type is not None:
        return list(database.find({"event_type": event_type}))

    if category is not None:
        return list(database.find({"category": category}))
    #seach for a particular event of the specified type
    #return the event as an object 
    # type is either "saving" or "spending"
    #return an array of matched events 
def add_event(event):
    if database.find_one({"id": event["id"]}):
        print(f"Event with this ID {event['id']} already exists")
        return
    database.insert_one(event)
    #add an event into the database
    #input is an dictionary containing all properties 
    #event={
    #    'id' : event_id
    #    'event_type': event_type,
    #    'title': title,
    #    'time': time,
    #    'quantity': quantity,
    #    'description': description,
    #    'category': category,
    #}
def modify_event(property, new_val):
    database.update_many({}, {"$set": {property: new_val}})
    #update all events with property=property to have new_val 
    #property:str new_val:str
def delete_event(property):
    events_collection.delete_one({"id": event_id})
    #delete an event with the specified property