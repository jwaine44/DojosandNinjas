from flask import Flask

app = Flask(__name__)

app.secret_key = "going to the secret dojo"           # Needs to be added for session; secret_key can be set to anything in the string

database = "dojos_and_ninjas_schema"