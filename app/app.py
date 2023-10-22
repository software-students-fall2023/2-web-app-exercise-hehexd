import db
import uuid
from flask import Flask, render_template, request, redirect, abort, url_for, make_response
from event import Event
import sort_and_filter as s
app=Flask(__name__)
#routes 
current_user = "admin"
#db.remove_one_user(current_user)
def calculate_total_spending(Acts):
    total = 0 
    for act in Acts:
        if act['event_type']=="spending":
            total+= act['quantity']
    return total 
def calculate_total_saving(Acts):
    total = 0 
    for act in Acts:
        if act['event_type']=="saving":
            total+= act['quantity']
    return total 
def calculate_net(Acts):
    total = 0 
    for act in Acts:
        if act['event_type']=="saving":
            total+= act['quantity']
        else:
            total-=act['quantity']
    return total 
@app.route('/')
def homepage(order = 1):
    sort = request.args.get('sortBy')
    order = request.args.get('order')
    start = request.args.get('start')
    end = request.args.get('end')
    list_event = db.get_events_for_user(current_user)
    #list_event = db.get_all_events()
    total_spending = calculate_total_spending(list_event)
    total_saving = calculate_total_saving(list_event)
    net_income = calculate_net(list_event)
    if (sort):
        if sort=="time":
            list_event=s.sort_by_time(list_event,int(order))
        elif sort == "amount":
            list_event=s.sort_by_amount(list_event,int(order))
    if (start and end):
        list_event = s.filter_by_time(list_event,start, end)
    #response = make_response(render_template('disAct.html',Acts=list_event))
    response=make_response(render_template("disAct.html", Acts=list_event, totalSpending=total_spending, totalSaving=total_saving, net=net_income), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/display-savings', methods=["GET"])
def display_savings():
    sort = request.args.get('sortBy')
    order = request.args.get('order')
    start = request.args.get('start')
    end = request.args.get('end')
    list_event = db.get_events_for_user(current_user)
    list_event = list(filter(s.is_saving,list_event))
    #list_event = db.get_all_events()
    total_spending = calculate_total_spending(list_event)
    total_saving = calculate_total_saving(list_event)
    net_income = calculate_net(list_event)
    if (sort):
        if sort=="time":
            list_event=s.sort_by_time(list_event,int(order))
        elif sort == "amount":
            list_event=s.sort_by_amount(list_event,int(order))
    if (start and end):
        list_event = s.filter_by_time(list_event,start, end)
    response=make_response(render_template("disAct.html", Acts=list_event, totalSaving=total_saving), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/display-spendings', methods=["GET"])
def display_spendings():
    sort = request.args.get('sortBy')
    order = request.args.get('order')
    start = request.args.get('start')
    end = request.args.get('end')
    list_event = db.get_events_for_user(current_user)
    list_event = list(filter(s.is_spending,list_event))
    #list_event = db.get_all_events()
    total_spending = calculate_total_spending(list_event)
    total_saving = calculate_total_saving(list_event)
    net_income = calculate_net(list_event)
    if (sort):
        if sort=="time":
            list_event=s.sort_by_time(list_event,int(order))
        elif sort == "amount":
            list_event=s.sort_by_amount(list_event,int(order))
    if (start and end):
        list_event = s.filter_by_time(list_event,start, end)
    response=make_response(render_template("disAct.html", Acts=list_event, totalSpending=total_spending), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-saving', methods=["GET"])
def display_add_saving_screen():
    response=make_response(render_template("addSav.html"), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/add-saving', methods=["POST"])
def add_saving():
    #TODO: function to add a saving event into the database AND the array events
    event_type = "saving"
    title = request.form['title']
    event_id = str(uuid.uuid4())
    time=request.form['time']
    quantity = int(request.form['quantity'])
    description = request.form['description']
    category = request.form.get('category')
    new_event={
        'user': current_user,
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
@app.route('/add-spending', methods=['POST'])
def add_spending():
    #TODO: function to add a spending event into the database AND the array events
    event_type = "spending"
    event_id = str(uuid.uuid4())
    title = request.form['title']
    time=request.form['time']
    quantity = int(request.form['quantity'])
    description = request.form['description']
    if (request.form.get('othertext')):
        category=request.form['othertext']
    else:
        category = request.form.get('category')
    new_event={
        'user': current_user,
        'event_id': event_id,
        'event_type': event_type,
        'title': title,
        'time': time,
        'quantity': quantity,
        'description': description,
        'category': category,
    }
    db.add_event(new_event)
    return redirect('/')
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
    print("edit act")
    event_id = request.args.get("id")
    title = request.form.get('title')
    time=request.form.get('time')
    quantity = int(request.form.get('quantity'))
    description = request.form.get('description')
    category = request.form.get('category')
    print("get all requested args")
    print(event_id,title,time,quantity,description,category)
    db.modify_event("title", title, event_id)
    db.modify_event("time", time, event_id)
    db.modify_event("quantity", quantity, event_id)
    db.modify_event("description", description, event_id)
    db.modify_event("category", category, event_id)
    return redirect('/')
@app.route('/search', methods=["GET"])
def show_search_event():
    filtered_events=None
    category= request.args.get("category") or 0
    ttype = request.args.get("type") or 0
    title = request.args.get("title") or 0 
    filtered_events=db.filter_acts(category, ttype, title)
    print(filtered_events)
    response=make_response(render_template("srch.html",Acts=filtered_events), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/settings', methods=["GET"])
def theme():
    response=make_response(render_template("theme.html", ), 200)
    response.mimetype = "text/html"
    return response 
'''
def show_settings():
    if (current_user!="None"):
        password=db.get_password(current_user)
    else:
        password = 0
    response=make_response(render_template("setting.html", password=password), 200)
    response.mimetype = "text/html"
    return response '''
@app.route('/settings', methods=["POST"])
def update_settings():
    if (request.form.get("delete")=="DELETE"):
        db.remove_one_user(current_user)
        current_user=None
        return (redirect('/'))
    new_password = request.form["new-password"]
    db.update_password(current_user, new_password)
    return (redirect('/'))
@app.route('/login', methods=["GET"])
def show_login():
    response=make_response(render_template("login.html", message=0), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/login', methods=["POST"])
def login():
    username = request.form["USERNAME"]
    passcode = request.form["PASSCODE"]
    status = db.login(username,passcode)
    if (status==0):
        response=make_response(render_template("login.html", message="username not found"), 200)
        return response
    elif (status==-1):
        response=make_response(render_template("login.html", message="wrong password"), 200)
        return response
    else:
        response=make_response(render_template("login.html", message="login success"), 200)
        current_user=username
        return response
@app.route('/register', methods=["GET"])
def show_register():
    response=make_response(render_template("register.html", message=0), 200)
    response.mimetype = "text/html"
    return response 
@app.route('/register', methods=["POST"])
def register():
    username = request.form["USERNAME"]
    passcode = request.form["PASSCODE"]
    status = db.add_new_user(username,passcode)
    if status == -1:
        response=make_response(render_template("register.html", message="user existed"), 200)
        return response
    else:
        response=make_response(render_template("register.html", message="successfully registered!"), 200)
        return response
@app.route('/delete', methods=["GET"])
def delete_act():
    event_id = request.args.get("id")
    print(event_id)
    db.delete_event(event_id)
    return (redirect('/'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
    #app.run(port=3000)