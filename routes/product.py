from flask import request, render_template
from models import Product, Inventory, Location
from database import db

def add_product():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    location_id = request.form['location_id']
    quantity = request.form['quantity']


    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()


    new_inventory = Inventory(product_id=new_product.id, location_id=location_id, quantity=quantity)
    db.session.add(new_inventory)
    db.session.commit()


    products_with_inventory = db.session.query(Product, Inventory, Location)\
        .join(Inventory, Product.id == Inventory.product_id)\
        .join(Location, Inventory.location_id == Location.id)\
        .all()
    locations = Location.query.all()

    return render_template('index.html', products_with_inventory=products_with_inventory, locations=locations)



def add_existing_product():
    existing_product_id = request.form['existing_product_id']
    location_id = request.form['location_id']
    quantity = request.form['quantity']

    existing_inventory = Inventory.query.filter_by(product_id=existing_product_id, location_id=location_id).first()

    new_inventory = Inventory(product_id=existing_product_id, location_id=location_id, quantity=quantity)
    db.session.add(new_inventory)
    db.session.commit()

    # Если успешно добавили, возвращаем список продуктов и локаций
    products_with_inventory = db.session.query(Product, Inventory, Location)\
        .join(Inventory, Product.id == Inventory.product_id)\
        .join(Location, Inventory.location_id == Location.id)\
        .all()

    products = Product.query.distinct(Product.name).all()
    locations = Location.query.all()

    return render_template('index.html', products = products, products_with_inventory = products_with_inventory, locations=locations)


