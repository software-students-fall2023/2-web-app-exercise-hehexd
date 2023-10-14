import db
from flask import Flask, render_template, request, redirect, abort, url_for, make_response

app=Flask(__name__)
#a global array of financial events 
events=db.get_all_events()
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
    response=make_response(render_template("home.html", list_event), 200)
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
    pass
@app.route('/add-spending', methods=["GET"])
def display_add_spending_screen():
    response=make_response(render_template("addSpending.html", events), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-spending', methods=["POST"])
def add_spending():
    #TODO: function to add a spending event into the database AND the array events
    pass





#run the app 
if __name__ == '__main__':
    app.run(port=3000)