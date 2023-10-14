#this module defined interactions with the mongodb database 
#its better to make all functions execute synchronously

def get_all_events():
    #return an array of all events in the database 
    pass
def search_event_type(type):
    #seach for a particular event of the specified type
    #return the event as an object 
    # type is either "saving" or "spending"
    #return an array of matched events 
    pass
def search_event_category(category):
    #seach for a particular event of the specified category 
    #return the event as an object 
    #return an array of matched events 
    pass
def add_event(event):
    #add an event into the database
    pass
def modify_event(property, new_val):
    #update all events with property=property to have new_val 
    pass
def delete_event():
    #delete an event 
    pass