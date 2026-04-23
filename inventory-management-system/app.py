from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

inventory = [
    {
        "id": 1,
        "name": "Milk",
        "price": 120,
        "stock": 20
    }
]

# Home
@app.route("/")
def home():
    return "Inventory API Running"


# GET all items
@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)


# GET one item
@app.route("/inventory/<int:id>", methods=["GET"])
def get_item(id):
    for item in inventory:
        if item["id"] == id:
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


# POST add item
@app.route("/inventory", methods=["POST"])
def add_item():
    data = request.get_json()

    new_item = {
        "id": len(inventory) + 1,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201


# PATCH update item
@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_item(id):
    for item in inventory:
        if item["id"] == id:

            data = request.get_json()

            item["price"] = data.get("price", item["price"])
            item["stock"] = data.get("stock", item["stock"])

            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404


# DELETE item
@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_item(id):
    for item in inventory:
        if item["id"] == id:
            inventory.remove(item)
            return jsonify({"message": "Deleted"})

    return jsonify({"error": "Item not found"}), 404


# OPEN FOOD FACTS
@app.route("/product/<barcode>", methods=["GET"])
def get_product(barcode):

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    response = requests.get(url)

    data = response.json()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5555)