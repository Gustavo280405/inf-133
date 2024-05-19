from database import db
class Book(db.Model):
    __tablename__ = "books"
    
    id=db.Column(db.Integer, primary_key=True)
    Title=db.Column(db.String(100), nullable=False)
    Author=db.Column(db.String(100), nullable=False)
    Edition=db.Column(db.Integer, nullable=False)
    Availability=db.Column(db.String(100), nullable=False)

def __init__(self, Title, Author, Edition, Availability):
    self.Title = Title
    self.Author = Author
    self.Edition = Edition
    self.Availability = Availability

def save(self):
    db.session.add(self)
    db.session.commit()

@staticmethod
def get_all():
    return Book.query.all()

@staticmethod
def get_by_id(id):
    return Book.query.get(id)

def update(self, Title=None, Author=None, Edition=None, Availability=None):
    if Title is not None:
        self.Title = Title
    if Author is not None:
        self.Author = Author
    if Edition is not None:
        self.Edition = Edition
    if Availability is not None:
        self.Availability = Availability
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()