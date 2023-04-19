# Auto-park

# DB ->
#       named as auto =>
#                       [ scheme of auto :
#                           {
#                              "label" : ... ,
#                              "price" : ... ,
#                              "wheels" : ... ,
#                              "color" : ... ,
#                              "number" : "random value"
#                           }
#                        ]

# Amount of auto > 10

# color : red , green , black , yellow , blue

# label : more than 5

# price : from 2000 till 200 000

# number and number length > 12

# Form category dictionary :
# dynamic

# cheap (2000 - 20000) , expensive(100000 - 200000) , medium - (20000 - 100000) - class car
# def sort_car_by_price (arr)
# return {
#   cheap : [],
#   medium : [],
#   expensive : []
# }


# print( cars that we have : for poor , rich , and medium-lvl persons )
# input -> sort : color -> choose on of : blue , green , ... ;  price , label


# for , while






import random

def exit() :
    result = input("Do you want quit? y/n : ") 
    return result.lower() 


class Car() :
    def __init__(self , label , price , color , wheels=str(4) , number=str(random.randint(1000 , 9999))):
        self.label = label
        self.price = price
        self.color = color
        self.wheels = wheels
        self.number = number

    def get_name(self) :
        beautiful_name = "|Label: " + self.label + '|  |Price: ' + self.price + '|  |Color: ' + self.color + '|  |Wheels: ' + self.wheels + '|  |Number: ' + self.number + '|'
        return beautiful_name.title()


test_car = Car("Audi" , "500" , "red")

print(test_car.get_name())

carsDB = [
    {
        "label" : "Toyota Camry",
        "price" : 19000,
        "wheels" : "",
        "color" : "red",
        "number" : str(random.randint(1000 , 9999))
    },
    {
        "label" : "Tesla Model x",
        "price" : 110000,
        "wheels" : "",
        "color" : "white",
        "number" : str(random.randint(1000 , 9999))
    },
    {
        "label" : "Ford Mustang",
        "price" : 45000,
        "wheels" : "",
        "color" : "yellow",
        "number" : str(random.randint(1000 , 9999))
    },
    {
        "label" : "Toyota Camry",
        "price" : 19000,
        "wheels" : "",
        "color" : "red",
        "number" : str(random.randint(1000 , 9999))
    },

]

# carsDB = Car()

# sorted_cars = sort_cars_by_price(autoDB)

# valid_colors = ["red" ,  "gree" , "black" , "pink"]
# for car in autoDB:
#     assert car["color"] in valid_colors


# auto.append(autoDB)

# def auto(label_auto , price_auto , wheels_auto , color_auto , number_auto) : 
#     {
#         "label": label_auto ,
#         "price": price_auto ,
#         "wheels" : wheels_auto,
#         "color": color_auto ,
#         "number": number_auto
#     }



# is_running = True

# while is_running :
#     user_choose = input("""
#         a) Show products
#         c) Registration
#         d) Authorization
#         q) Exit
#     Answer : """).lower()

#     if user_choose == "a" :
#         print_cars(carsDB)

#     elif user_choose == "q" :
#         result = exit() 
#         if result == "y" :
#             is_running = False

