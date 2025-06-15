from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    reviews = db.relationship('Review', back_populates='customer')
    items = db.relationship('Item', secondary='reviews', back_populates='customers', viewonly=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "reviews": [review.id for review in self.reviews]
        }

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    reviews = db.relationship('Review', back_populates='item')
    customers = db.relationship('Customer', secondary='reviews', back_populates='items', viewonly=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "reviews": [review.id for review in self.reviews]
        }

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    rating = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')

    def to_dict(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "rating": self.rating,
            "customer_id": self.customer_id,
            "item_id": self.item_id,
            "customer": {
                "id": self.customer.id,
                "name": self.customer.name
            } if self.customer else None,
            "item": {
                "id": self.item.id,
                "name": self.item.name,
                "price": self.item.price
            } if self.item else None
        }