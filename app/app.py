import db
import uuid
from flask import Flask, render_template, request, redirect, abort, url_for, make_response
from event import Event

app=Flask(__name__)
#routes 
@app.route('/')
def homepage():
    display = request.args.get('display')
    sort = request.args.get('sortBy')
    filterr = request.args.get('filter')
    if (display=="savingOnly"):
        list_event=db.search_event_type("saving")
    elif (display=="spendingOnly"):
        list_event=db.search_event_type("saving")
    else:
        list_event = db.get_all_events()
    if (sort):
        pass
    if (filterr):
        pass
    response=make_response(render_template("displayExpenses.html", expenses=list_event), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-saving', methods=["GET"])
def display_add_saving_screen():
    response=make_response(render_template("addSaving.html", events), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-saving', methods=["POST"])
def add_saving():
    #TODO: function to add a saving event into the database AND the array events
    event_type = "saving"
    title = request.form['title']
    event_id = str(uuid.uuid4())
    time=request.form['time']
    quantity = request.form['quantity']
    description = request.form['description']
    category = 0
    new_event={
        'event_id': event_id,
        'event_type': event_type,
        'title': title,
        'time': time,
        'quantity': quantity,
        'description': description,
        'category': category,
    }
    db.add_event(new_event)
    return(redirect('/'))
@app.route('/add-spending', methods=["GET"])
def display_add_spending_screen():
    response=make_response(render_template("addSpending.html"), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-spending', methods=["POST"])
def add_spending():
    #TODO: function to add a spending event into the database AND the array events
    event_type = "spending"
    event_id = str(uuid.uuid4())
    title = request.form['title']
    time=request.form['time']
    quantity = request.form['quantity']
    description = request.form['description']
    category = request.form['category']
    new_event={
        'event_id': event_id,
        'event_type': event_type,
        'title': title,
        'time': time,
        'quantity': quantity,
        'description': description,
        'category': category,
    }
    db.add_event(new_event)
    return(redirect('/'))
@app.route('/event', methods=["GET"])
def display_event():
    event = request.args.get(event)
    response=make_response(render_template("event.html", event), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/modifyEvent', methods=["GET"])
def show_modify_event():
    event_id = request.args["id"]
    response=make_response(render_template("modify.html", event), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/modifyEvent',methods=["POST"])
def modify_event():
    pass


#run the app
if __name__ == '__main__':
    app.run(port=3000)