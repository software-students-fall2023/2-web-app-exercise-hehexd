import db
import uuid
from flask import Flask, render_template, request, redirect, abort, url_for, make_response
from event import Event
import sort_and_filter as s
app=Flask(__name__)
#routes 
@app.route('/')
def homepage(order = 1):
    sort = request.args.get('sortBy')
    order = request.args.get('order')
    start = request.args.get('start')
    end = request.args.get('end')
    list_event = db.get_all_events()
    if (sort):
        if sort=="time":
            list_event=s.sort_by_time(list_event,int(order))
        elif sort == "amount":
            list_event=s.sort_by_amount(list_event,int(order))
    if (start and end):
        list_event = s.filter_by_time(list_event,start, end)
    response=make_response(render_template("disAct.html", Acts=list_event), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-saving', methods=["GET"])
def display_add_saving_screen():
    response=make_response(render_template("addSaving.html"), 200)
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
    response=make_response(render_template("addAct.html"), 200)
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
@app.route('/act', methods=["GET"])
def display_event():
    event_id = request.args.get("id")
    this_event= db.search_event("event_id",event_id)
    print(this_event)
    response=make_response(render_template("viewAct.html", act=this_event), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/editAct', methods=["GET"])
def show_modify_event():
    event_id = request.args["id"]
    act = db.search_event("event_id",event_id)
    response=make_response(render_template("editAct.html", act=act), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/editAct',methods=["POST"])
def modify_event():
    event_id = request.args["id"]
    event_type = request.form['type']
    title = request.form['title']
    time=request.form['time']
    quantity = request.form['quantity']
    description = request.form['description']
    category = request.form['category']
    modify_event("event_type",event_type,event_id)
    modify_event("title", title, event_id)
    modify_event("time", time, event_id)
    modify_event("quantity", quantity, event_id)
    modify_event("description", description, event_id)
    modify_event("category", category, event_id)
    return 
@app.route('/searchEvent', methods=["GET"])
def show_search_event():
    response=make_response(render_template("srch.html"), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/settings', methods=["GET"])
def show_settings():
    response=make_response(render_template("setting.html"), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/login', methods=["GET"])
def show_login():
    response=make_response(render_template("login.html"), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/login', method=["POST"])
def login():
    username = request.form["USERNAME"]
    passcode = request.form["PASSCODE"]
    if (db.login(username, passcode)==0):
        print("username unfound")
    elif (db.login(username,passcode)==-1):
        print("wrong passcode")
    else:
        pass
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
    #app.run(port=3000)