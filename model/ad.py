class Ad(object):

    def __init__(self, ad_id, title, description, price, date, is_active, owner=None):
        self.ad_id = ad_id
        self.title = title
        self.description = description
        self.price = price
        self.date = date
        self.is_active = is_active
        self.owner = owner
