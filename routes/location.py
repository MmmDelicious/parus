from flask import request, jsonify, render_template
from models import Location, Product, Inventory
from database import db

def add_location():
    name = request.form['name']


    new_location = Location(name=name)
    db.session.add(new_location)
    db.session.commit()


    products_with_inventory = db.session.query(Product, Inventory, Location)\
        .join(Inventory, Product.id == Inventory.product_id)\
        .join(Location, Inventory.location_id == Location.id)\
        .all()
    locations = Location.query.all()

    return render_template('index.html', products_with_inventory=products_with_inventory, locations=locations)