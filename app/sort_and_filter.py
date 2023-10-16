def sort_by_time(events, order):
    #   helper function that will sort the input events according to time
    #   events is a list of dictionaries
    #   each dictrionary has those properties: 
    #{
    #    'event_id': event_id,
    #    'event_type': event_type,
    #    'title': title,
    #    'time': time,
    #    'quantity': quantity,
    #    'description': description,
    #    'category': category,
    #}
    # so for each event, access time with event.time 
    # time is in format of a string "YYYY-MM-DD"
    # order is an integer, order > 1 means sort in ascending order, <1 means sort in descending order
    # u can either do that in place or return a new copy of the array 
    if order >= 0:
        #Ascending
        sorted_events = sorted(events, key=lambda event: event['time'])
    else:
        #Descending order
        sorted_events = sorted(events, key=lambda event: event['time'], reverse=True)
    
    return sorted_events
    
def sort_by_amount(events, order):
    #basically the same as the one above but sort based on amount of money instead
    #that is given by event.quantity. quantity is a float. 
    # please make sure to push it from another branch with pull requests 
    if order >= 0:
        #Ascending
        sorted_events = sorted(events, key=lambda event: event['quantity'])
    else:
        #Descending order
        sorted_events = sorted(events, key=lambda event: event['quantity'], reverse=True)
    
    return sorted_events
    
def filter_by_time(events, start, end):
    #filter the given list of events, keeps only events that happens in between start and end. returns a new filtered list 
    #still, start and end takes the format of "YYYY-MM-DD"
    # if start == end, return the events which has time == start == end 
    #maybe helpful to use filter()
    if start == end:
        filtered_events = filter(lambda event: event['time'] == start, events)
    else:
        # Filter events that have 'time' within the range [start, end]
        filtered_events = filter(lambda event: start <= event['time'] <= end, events)
    
    # Convert the filter object to a list to return the result
    return list(filtered_events)
def is_saving(event):
    return (event.event_type == "saving")
def is_spending(event):
    return (event.event_type == "spending")