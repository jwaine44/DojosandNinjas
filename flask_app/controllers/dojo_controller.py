from venv import create
from flask import session, render_template, request, redirect
from flask_app import app

from flask_app.models.dojo_model import Dojo

@app.route('/')
@app.route('/dojos')
def display_dojos():
    all_dojos = Dojo.get_all_dojos()
    return render_template("dojo.html", dojos = all_dojos)

@app.route('/dojos/<int:id>')
def show_single_dojo(id):
    data = {
        'id': id
    }
    dojo = Dojo.display_dojo(data)
    return render_template("ninjasindojo.html", dojo = dojo)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos') 