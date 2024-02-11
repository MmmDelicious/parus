from flask import request, render_template
from models import Product, Inventory, Location
from database import db


def filter_products_by_location():
    search_query = request.form.get('searchInput')
    print(search_query)
    if search_query == 'all':
        products = db.session.query(Product, Inventory, Location)\
            .join(Inventory, Product.id == Inventory.product_id)\
            .join(Location, Inventory.location_id == Location.id)\
            .all()
    else:
        products = db.session.query(Product, Inventory, Location)\
            .join(Inventory, Product.id == Inventory.product_id)\
            .join(Location, Inventory.location_id == Location.id)\
            .filter(Product.name.ilike(f"%{search_query}%"))\
            .all()

    locations = Location.query.all()

    return render_template('index.html', products_with_inventory=products, locations=locations)

def filter_products_by_price():

    products = db.session.query(Product, Inventory, Location) \
        .join(Inventory, Product.id == Inventory.product_id) \
        .join(Location, Inventory.location_id == Location.id) \
        .order_by(Product.price.desc()) \
        .all()

    locations = Location.query.all()

    return render_template('index.html', products_with_inventory=products, locations=locations)


def filter_products_by_count():
    products = db.session.query(Product, Inventory, Location) \
        .join(Inventory, Product.id == Inventory.product_id) \
        .join(Location, Inventory.location_id == Location.id) \
        .order_by(Inventory.quantity.desc()) \
        .all()

    locations = Location.query.all()

    return render_template('index.html', products_with_inventory=products, locations=locations)