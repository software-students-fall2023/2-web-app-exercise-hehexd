import random
#this module defined interactions with the mongodb database 
#its better to make all functions execute synchronously
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://2SEProjectDatabase:ThisIsThePassword123@cluster0.21yazmx.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, tlsAllowInvalidCertificates=True, server_api=ServerApi('1'))
databaseclient = client["account"]
database = databaseclient['account']
collection = databaseclient["Username+Password"]
def get_all_events():
    return list(database.find({}))
    #return an array of all events in the database 
def search_event(sproperty, val):
    '''
    if type is not None:
        return list(database.find({"event_type": event_type}))

    if category is not None:
        return list(database.find({"category": category}))
    '''
    if (sproperty):
        return database.find_one({sproperty: val})
    #seach for a particular event of the specified type
    #return the event as an object 
    # type is either "saving" or "spending"
    #return an array of matched events 
def search_event_list(sproperty, val):
    if (sproperty):
        return list(database.find({sproperty: val}))
def add_event(event):
    if database.find_one({"event_id": event["event_id"]}):
        print(f"Event with this ID {event['id']} already exists")
        return
    database.insert_one(event)
    #add an event into the database
    #input is an dictionary containing all properties 
    #event={
    #    'event_id' : event_id
    #    'event_type': event_type,
    #    'title': title,
    #    'time': time,
    #    'quantity': quantity,
    #    'description': description,
    #    'category': category,
    #}
def modify_event(property, new_val, event_id):
    database.update_many({"event_id": event_id}, {"$set": {property: new_val}})
    #update all events with property=property to have new_val 
    #property:str new_val:str
def delete_event(event_id):
    database.delete_one({"event_id": event_id})
    #delete an event with the specified property
def clear_collection():
    database.delete_many({})
    #erase everything in the db and start over! 
def login(username, password):
    user = collection.find_one({"username": username})
    if not user:
        return 0
    elif user["password"] != password:
        return -1
    else:
        return 1
    # search in the username/databse collection 
    # if username does not exist, return 0 
    # if username exist but password does not match, return -1 
def add_new_user(username, password):
    if collection.find_one({"username": username}):
        return -1
    user = {
        "username": username,
        "password": password,
    }
    collection.insert_one(user)
    return 1
    #add username and password pairs to the database
    #if username already exists, return -1 
def remove_user(username):
    collection.delete_one({"username": username})
def get_password(username):
    return collection.find_one({"username":username})["password"]
def update_password(username, password):
    collection.update_one({"username": username}, {"$set": {"password": password}})
def filter_acts(category, type, title):
    query = {}
    if category:
        query["category"] = category
    if type:
        query["type"] = type
    if title:
        query["title"] = {"$regex": title, "$options": "i"}
    return list(database.find(query))
    #return all events that has the specified category, type, and whose title contains title (the argument 
    # category, type, title can be 0. in that case ignore 
def get_events_for_user(username):
    #get all activities associated with this userid. AND user named "admin"
    return list(database.find({"$or": [{"user": username}, {"user": "admin"}]}))
def remove_one_user(username):
    #delete all activities associated with this user
    database.delete_many({"user": username})
#print(get_all_events())
#(sproperty,val) = ("event_id", 2)
#print(database.find_one({sproperty:val}))