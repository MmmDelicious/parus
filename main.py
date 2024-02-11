from app import app
from models import Product, Location, Inventory
from database import db


#заполнение бд
def fill_database():
    with app.app_context():

        #db.create_all();

        product1 = Product(name='Product 1', description='Description 1', price=10.0)
        product2 = Product(name='Product 2', description='Description 2', price=20.0)
        product3 = Product(name='Product 3', description='Description 3', price=30.0)
        product4 = Product(name='Product 4', description='Description 4', price=40.0)
        product5 = Product(name='Product 5', description='Description 5', price=50.0)
        product6 = Product(name='Product 6', description='Description 6', price=60.0)

        location1 = Location(name='Location 1')
        location2 = Location(name='Location 2')
        location3 = Location(name='Location 3')
        location4 = Location(name='Location 4')
        location5 = Location(name='Location 5')
        location6 = Location(name='Location 6')

        inventory1 = Inventory(product=product1, location=location1, quantity=100)
        inventory2 = Inventory(product=product2, location=location2, quantity=200)
        inventory3 = Inventory(product=product3, location=location3, quantity=300)
        inventory4 = Inventory(product=product4, location=location4, quantity=400)
        inventory5 = Inventory(product=product5, location=location5, quantity=500)
        inventory6 = Inventory(product=product6, location=location6, quantity=600)

        db.session.add_all([product1, product2, product3, location1, location2, location3, inventory1, inventory2, inventory3])
        db.session.add_all([product4, product5, product6, location4, location5, location6, inventory4, inventory5, inventory6])

        db.session.commit()

if __name__ == "__main__":
    fill_database()
