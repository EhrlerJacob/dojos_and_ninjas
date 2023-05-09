from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
# dojo.ninjas.append(ninja.Ninja(ninja_data))

class Dojo:
    db = "dojos_and_ninjas_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod 
    def create_dojo(cls,data):
        query ="""
        INSERT INTO dojos
        (name) VALUES(%(name)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos=[]
        for i in results:
            dojos.append(cls(i))
        return dojos
    
    @classmethod
    def get_one_dojo(cls,data):
        query= """
            SELECT * FROM dojos
            WHERE id= %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = """
        SELECT * FROM dojos
        LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id 
        WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

        dojo = cls(results[0])
        for row_from_db in results:

                data= {
                    'id':row_from_db['ninjas.id'],
                    'first_name':row_from_db['first_name'],
                    'last_name':row_from_db['last_name'],
                    'age':row_from_db['age'],
                    'created_at':row_from_db['created_at'],
                    'updated_at':row_from_db['updated_at'],
                    'dojos_id':row_from_db['dojos_id']
                }
                dojo.ninjas.append(ninja.Ninja(data))
        return dojo
        