from flask import Blueprint, request, jsonify

products_bp = Blueprint('products', __name__)

# In-memory "database", can be replaced with realtime database
products = []
next_id = 1

@products_bp.route('/', methods=['GET'])
def get_products():
    """
    GET /products
    Returns the full list of products.
    """
    return jsonify(products), 200

@products_bp.route('/', methods=['POST'])
def add_product():
    """
    POST /products
    Accepts JSON data with 'name' and 'price' fields and adds a new product.
    Returns the newly created product with its unique id.
    """
    global next_id
    data = request.get_json()

    # Validate input
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Missing 'name' or 'price' in request body"}), 400

    # Create and store the product
    product = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(product)
    next_id += 1

    return jsonify(product), 201
