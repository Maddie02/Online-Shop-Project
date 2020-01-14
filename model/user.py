from database import SQLite

class User(object):
    
    def __init__(self, id, email, password, name, address, phone_number):
        self.id = id
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
            if self.id == None: 
                values = (self.email, self.password, self.name, self.address, self.phone_number)
                db.execute("INSERT INTO user (email, password, name, address, phone_number) VALUES (?, ?, ?, ?, ?)", values)
                return self
            else:
                values = (self.id, self.email, self.password, self.name, self.address, self.phone_number)
                db.execute("REPLACE INTO user (id, email, password, name, address, phone_number) VALUES (?, ?, ?, ?, ?, ?)", values)
                return self

    @staticmethod
    def find_by_id(id):
        with SQLite() as db:
            result = db.execute("SELECT * FROM user WHERE id = ?", (id, )).fetchone()
            return User(*result)

    @staticmethod
    def get_all():
        result = None
        with SQLite() as db:
            result = db.execute("SELECT id, email, password, name, address, phone_number FROM user").fetchall()
            return [User(*row) for row in result]
    
    @staticmethod
    def delete(id):
        result = None
        with SQLite() as db:
            result = db.execute("DELETE FROM user WHERE id = ?", (id, ))
    
     
