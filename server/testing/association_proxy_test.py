from app import app, db
from server.models import Customer, Item, Review

class TestAssociationProxy:
    '''Customer in models.py'''

    def test_has_association_proxy(self):
        '''has association proxy to items'''
        with app.app_context():
            db.drop_all()
            db.create_all()
            # Create a customer and an item
            c = Customer(name="Test Customer")
            i = Item(name="Test Item", price=1.0)
            db.session.add_all([c, i])
            db.session.commit()

            # Create a review linking the customer and item
            r = Review(comment='great!', customer=c, item=i)
            db.session.add(r)
            db.session.commit()

            # Check association proxy
            assert hasattr(c, 'items')
            assert i in c.items