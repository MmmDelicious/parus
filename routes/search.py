from flask import request, render_template
from models import Product, Inventory, Location
from database import db

def search_products():
    if request.method == 'POST':
        search_query = request.form.get('searchInput')

        if search_query:
            products_with_inventory = db.session.query(Product, Inventory, Location)\
                .join(Inventory, Product.id == Inventory.product_id)\
                .join(Location, Inventory.location_id == Location.id)\
                .filter(Product.name.ilike(f"%{search_query}%"))\
                .all()
        else:
            products_with_inventory = db.session.query(Product, Inventory, Location)\
                .join(Inventory, Product.id == Inventory.product_id)\
                .join(Location, Inventory.location_id == Location.id)\
                .all()

        locations = Location.query.all()

        return render_template('product_table.html', products_with_inventory=products_with_inventory, locations=locations)


    return render_template('index.html')