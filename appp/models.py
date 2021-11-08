from appp import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), index = True, unique = True)
    rank = db.Column(db.Integer, index = True)
    visited = db.Column(db.Boolean)
    
    def __repr__(self):
        return '<City {}>'.format(self.city)
    
    def __init__(self, city_e, rank_e, visited_e):
        self.city=city_e
        self.rank=rank_e
        self.visited=visited_e