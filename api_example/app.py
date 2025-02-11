from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {
            "id": "1",
            "name": "Product 1",
            "category": "Electronics",
            "price": 199.99,
            "stock": 25,
            "rating": 4.5,
            "description": "A high-quality electronic device."
        },
        {
            "id": "2",
            "name": "Product 2",
            "category": "Home Appliance",
            "price": 89.99,
            "stock": 50,
            "rating": 4.2,
            "description": "Durable and energy-efficient home appliance."
        },
        {
            "id": "3",
            "name": "Product 3",
            "category": "Books",
            "price": 15.99,
            "stock": 100,
            "rating": 4.8,
            "description": "A bestselling novel with great reviews."
        },
       
    ]

    return {
        "success": True,
        "message": "Products fetched successfully",
        "data": products
    }

if __name__ == "__main__":
    app.run(debug=True)
