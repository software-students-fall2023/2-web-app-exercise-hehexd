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
    pass
def sort_by_amount(events, order):
    #basically the same as the one above but sort based on amount of money instead
    #that is given by event.quantity. quantity is a float. 
    # please make sure to push it from another branch with pull requests 
    pass
def filter_by_time(events, start, end):
    #filter the given list of events, keeps only events that happens in between start and end. returns a new filtered list 
    #still, start and end takes the format of "YYYY-MM-DD"
    # if start == end, return the events which has time == start == end 
    #maybe helpful to use filter()
    pass