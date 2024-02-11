from flask import render_template
from models import Product, Location, Inventory
from database import db

def index():
    products_with_inventory = db.session.query(Product, Inventory, Location)\
        .join(Inventory, Product.id == Inventory.product_id)\
        .join(Location, Inventory.location_id == Location.id)\
        .all()
    locations = Location.query.all()
    products = Product.query.all()
    inventory = Inventory.query.all()
    return render_template('index.html', products_with_inventory=products_with_inventory, locations=locations, products=products, inventory=inventory)
