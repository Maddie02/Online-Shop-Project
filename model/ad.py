from database import SQLite

class Ad(object):

    def __init__(self, id, title, description, price, date, is_active, owner_id):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.date = date
        self.is_active = is_active
        self.owner_id = owner_id

    def to_dict(self):
        ad_data = self.__dict__
        return ad_data 
   
    def save(self):
        with SQLite() as db:
            if self.id == None:
                values = (self.title, self.description, self.price, self.date, self.is_active, self.owner_id)
                db.execute("INSERT INTO ad (title, description, price, date, is_active, owner_id) VALUES (?, ?, ?, ?, ?, ?)", values)
                return self
            else:
                values = (self.id, self.title, self.description, self.price, self.date, self.is_active, self.owner_id)
                db.execute("REPLACE INTO ad (id, title, description, price, date, is_active, owner_id) VALUES (?, ?, ?, ?, ?, ?, ?)", values)
                return self

    @staticmethod
    def get_all():
        result = None
        with SQLite() as db:
            result = db.execute("SELECT * FROM ad").fetchall()
            return [Ad(*row) for row in result]
    
    @staticmethod
    def find_by_id(id):
        with SQLite() as db:
            result = db.execute("SELECT * FROM ad WHERE id = ?", (id, )).fetchone()
            return Ad(*result)