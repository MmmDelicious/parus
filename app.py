from flask import Flask
from database import db
from routes import index, location, search, product, inventory, filters
from constants import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



app.add_url_rule('/', view_func=index.index)
app.add_url_rule('/add_product', view_func=product.add_product, methods=['POST'])
app.add_url_rule('/add_existing_product', view_func=product.add_existing_product, methods=['POST'])
app.add_url_rule('/add_location', view_func=location.add_location, methods=['POST'])
app.add_url_rule('/search', view_func=search.search_products, methods=['GET', 'POST'])
app.add_url_rule('/change_inventory', view_func=inventory.change_inventory, methods=['POST'])
app.add_url_rule('/filter_products', view_func=filters.filter_products_by_location, methods=['GET', 'POST'])
app.add_url_rule('/sorted_by_price', view_func=filters.filter_products_by_price, methods=['GET'])
app.add_url_rule('/sorted_by_count', view_func=filters.filter_products_by_count, methods=['GET'])

if __name__ == "__main__":
    app.run(debug=True)
