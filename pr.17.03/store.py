# 1) Store
# 2) Into store you might : a) Category ( [] )
#    b) Show All products
#    c) Admin mode
#    q) Quit
# if a) -> a) TV , b) Smartphone , c) Mp3 , d) DvD
#       a -> show all TV []
#       b -> show all Sm []
#       c -> show all Mp3 []
# products are dictionaries :
# { "label" : "..." , "price" : "..." , desc : ""... }
# 3) User might buy product if user has money (
#                   {
#                   "name" : "..." ,
#                   "money" : ... ,
#                   "bag" : []
#                   }
# )
# 4) Admin mode yields ->
#   1) add product to category ,
#   2) Delete product
#   3) Change name of product


store = {
    "TV": [
        {
            "product" : "Samsung" ,
            "price" : 100
        }
    ],
        "Smartphone": [
        {
            "product" : "Pixel" ,
            "price" : 100
        }
    ],
        "Mp3": [
        {
            "product" : "Walkman" ,
            "price" : 100
        }
    ],
        "DvD": [
        {
            "product" : "Sony" ,
            "price" : 100
        }
    ]
    
}



user_name = input("Hello, what is your name? : ")

user_money = input("How moch money do you have? :")

user = {
    "name" : user_name ,
    "money" : user_money ,
    "bag" : []
}


def sorting() :
    for key, value in store.items() :
        if key == "TV" :
            return value ,
        elif key == "Smartphone" :
            return value  ,
        elif key == "Mp3" :
            return value  , 
        elif key == "DvD" :
            return value  ,


is_running = True

while is_running :
    user_choose = input("""
        a) Category
        b) Show All products
        c) Admin mode
        q) Quit
    Answer : """).lower()

    if user_choose == "a" :
        print(sorting())