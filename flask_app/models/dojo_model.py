from sqlite3 import connect
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def display_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        single_result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        ninjas = []

        for ninja in single_result:
            ninjas.append(Ninja(ninja))

        return ninjas

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT into dojos(name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

# JOIN for ninjasindojo
# flask_app.models import ninja_model to import Ninja into it
# it'll show in ninjasindojo.html