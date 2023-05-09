from flask_app import app
from flask_app.models import dojo, ninja
from flask import redirect, render_template, request


@app.route('/ninjas/new')
def new_ninja():
    dojos = dojo.Dojo.get_all()
    return render_template("new_ninja.html", all_dojos = dojos)

@app.route('/ninjas/create', methods = ['POST'])
def save_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id':request.form['dojos_id'],
    }
    ninja.Ninja.create_ninja(data)
    return redirect ('/dojos')



