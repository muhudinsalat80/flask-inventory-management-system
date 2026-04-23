import requests

base_url = "http://127.0.0.1:5555"

print("1. View Inventory")
print("2. Add Item")

choice = input("Choose: ")

if choice == "1":
    response = requests.get(base_url + "/inventory")
    print(response.json())

elif choice == "2":
    name = input("Name: ")
    price = int(input("Price: "))
    stock = int(input("Stock: "))

    data = {
        "name": name,
        "price": price,
        "stock": stock
    }

    response = requests.post(base_url + "/inventory", json=data)

    print(response.json())