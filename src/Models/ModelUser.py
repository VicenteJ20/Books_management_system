from .Entities.User import User

class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            query = "SELECT rut, password, fullname FROM administrador WHERE rut = '{}'".format(user.id)
            cursor.execute(query)
            row = cursor.fetchone()
            if row != None:
                myuser = User(row[0], User.check_password(row[1], user.password), row[2])
                return myuser
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_rut(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "SELECT rut, fullname FROM administrador WHERE rut = '{}'".format(id)
            cursor.execute(query)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], None, row[1])
            else:
                return None
        except Exception as ex:
            raise Exception(ex)