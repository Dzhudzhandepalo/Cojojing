import random

# DB
auto = [
    {"label": "Toyota Camry", "price": 25000, "wheels": 4, "color": "red", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Honda Accord", "price": 22000, "wheels": 4, "color": "green", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Ford Mustang", "price": 35000, "wheels": 4, "color": "black", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Nissan GT-R", "price": 120000, "wheels": 4, "color": "yellow", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "BMW M3", "price": 45000, "wheels": 4, "color": "blue", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Mercedes-Benz S-Class", "price": 100000, "wheels": 4, "color": "black", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Audi A6", "price": 35000, "wheels": 4, "color": "red", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Lamborghini Huracan", "price": 200000, "wheels": 4, "color": "yellow", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Porsche 911", "price": 90000, "wheels": 4, "color": "green", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Ferrari 488", "price": 180000, "wheels": 4, "color": "red", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Chevrolet Camaro", "price": 30000, "wheels": 4, "color": "blue", "number": str(random.randint(1000000000000, 9999999999999))},
    {"label": "Dodge Challenger", "price": 28000, "wheels": 4, "color": "black", "number": str(random.randint(1000000000000, 9999999999999))}
]

# Amount of auto > 10
assert len(auto) > 10

# color : red , green , black , yellow , blue
valid_colors = ["red", "green", "black", "yellow", "blue"]
for car in auto:
    assert car["color"] in valid_colors

# label : more than 5
for car in auto:
    assert len(car["label"]) > 5

# price : from 2000 till 200 000
for car in auto:
    assert car["price"] >= 2000 and car["price"] <= 200000

# number and number length > 12

# Amount of auto > 10
assert len(auto) > 10

# color : red , green , black , yellow , blue
valid_colors = ["red", "green", "black", "yellow", "blue"]
for car in auto:
    assert car["color"] in valid_colors

# label : more than 5
for car in auto:
    assert len(car["label"]) > 5

# price : from 2000 till 200 000
for car in auto:
    assert car["price"] >= 2000 and car["price"] <= 