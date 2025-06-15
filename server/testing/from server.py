from server.app import db

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    reviews = db.relationship('Review', back_populates='customer')
    items = db.relationship('Item', secondary='reviews', viewonly=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "reviews": [review.id for review in self.reviews],
            "items": [item.id for item in self.items]
        }

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    reviews = db.relationship('Review', back_populates='item')

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
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')

    def to_dict(self):
        return {
            "id": self.id,
            "comment": self.comment,
            "customer_id": self.customer_id,
            "item_id": self.item_id
        }