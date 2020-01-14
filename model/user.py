from database import SQLite

class User(object):
    
    def __init__(self, email, password, name, address, phone_number, user_id = None):
        self.id = user_id
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def to_dict(self):
        user_data = self.__dict__
        return user_data 

    def save(self):
        with SQLite() as db:
            values = (self.id, self.email, self.password, self.name, self.address, self.phone_number)
            db.execute("INSERT INTO user (id, email, password, name, address, phone_number) VALUES (?, ?, ?, ?, ?, ?)", values)
            return self

    @staticmethod
    def find_by_id(user_id):
        result = None
        with SQLite() as db:
            result = db.execute("SELECT email, password, name, address, phone_number FROM user WHERE id = ?", (user_id, ))
        user = result.fetchone()
        return User(*user)

    @staticmethod
    def get_all():
        result = None
        with SQLite() as db:
            result = db.execute("SELECT id, email, password, name, address, phone_number FROM user").fetchall()
            return [User(*row) for row in result]
    
    @staticmethod
    def delete(user_id):
        result = None
        with SQLite() as db:
            result = db.execute("DELETE FROM user WHERE id = ?", (user_id, ))
    
     
