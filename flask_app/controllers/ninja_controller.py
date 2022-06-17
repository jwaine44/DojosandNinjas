from flask import session, render_template, request, redirect
from flask_app import app

from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

# import Dojo here to access Dojo info

@app.route('/ninjas')
def display_new_ninja():
    all_dojos = Dojo.get_all_dojos()
    return render_template("ninja.html", dojos = all_dojos)

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    num = request.form['dojo_id']
    Ninja.create_ninja(request.form)
    return redirect(f'/dojos/{num}')

# drop down for Add Ninja^^^^^

@app.route('/dojos/<int:id>/show')
def get_ninja_by_dojo_id():
    data = {
        "dojo_id": dojo_id
    }
    ninja = Ninja.get_one(data)
    return render_template('ninjasindojo.html', ninja = ninja)