from flask_app import app
from flask import redirect, render_template, request
from flask_app.models import dojo 

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos_dashboard():
    return render_template("dojos_dashboard.html", dojos=dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/show/<int:id>')
def show_dojo(id):
    data ={
        'id':id
    }
    return render_template("show_dojo.html", one_dojo=dojo.get_one_dojo(data))