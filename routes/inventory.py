from flask import request, jsonify
from models import Inventory
from database import db

def change_inventory():
    productId = request.form.get('productId')
    locationId = request.form.get('locationId')
    action = request.form.get('action')
    quantity = int(request.form.get('quantity'))

    inventory = Inventory.query.filter_by(product_id=productId, location_id=locationId).first()

    if inventory:
        if action == 'add':
            inventory.quantity += quantity
        elif action == 'remove' and inventory.quantity >= quantity:
            inventory.quantity -= quantity

        db.session.commit()

        return jsonify({'newCount': inventory.quantity}), 200
