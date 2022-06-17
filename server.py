from flask import Flask      # request and redirect are needed on 'POST' routes; session keeps track the amount of times the page has been visited; session is an empty dictionary
from flask_app import app       #Importing app variable from __init__.py

#Import all controllers in controllers folder
from flask_app.controllers import dojo_controller
from flask_app.controllers import ninja_controller


if __name__ == "__main__":
    app.run(debug = True)
# This code is needed to run your environment and be in an active state when you run this file.