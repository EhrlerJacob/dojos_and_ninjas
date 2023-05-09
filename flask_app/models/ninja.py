from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = "dojos_and_ninjas_schema"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_ninjas(cls):
        query= """
        SELECT * FROM ninjas;
        """
        results = connectToMySQL(cls.db).query_db(query)

        all_ninjas = []

        for ninja in results:
            all_ninjas.append(cls(ninja))

        return all_ninjas

    @classmethod
    def get_one_ninja(cls,data):
        query = """
        SELECT * FROM ninjas 
        WHERE id = %(id)s;
        """
        results=connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_ninja(cls,data):
        query ="""
        INSERT INTO ninjas
        (first_name, last_name, age, dojos_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)
    
    
    
