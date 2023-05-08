from flask_app import app
from flask_app.models import dojo, ninja
from flask import redirect, render_template, request


@app.route('/ninjas/new')
def new_ninja():
    dojos = dojo.Dojo.get_all()
    return render_template("new_ninja.html", all_dojos = dojos)

@app.route('ninjas/create', methods = ['POST'])
def create_ninja():
    return redirect ('/dojos')



