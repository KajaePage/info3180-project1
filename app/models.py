import unicodedata
from . import db
from werkzeug.security import generate_password_hash

class propertyProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedrooms = db.Column(db.String(3)) 
    bathroom = db.Column(db.String(3))
    location = db.Column(db.String(255))
    price = db.Column(db.String(20))
    type = db.Column(db.String(10))
    description = db.Column(db.String(255))
    filename = db.Column(db.String(255))

    def __init__(self, title, bedrooms, bathroom, location, price, type, description, filename):
        self.title = title
        self.bedrooms = bedrooms
        self.bathroom = bathroom
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.filename = filename
    