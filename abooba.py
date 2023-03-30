

users_base = []

def registration (name , age , wallet):
    return {
        "name" : name,
        "age" : age,
        "wallet": wallet
    }

def how_old():
    if int(age) >= 18:
        return True
    else:
        print("Bocome older")
        

def name_lenght():
    if len(name) >= 5 continue
        
    else:
        print("Name must be more than 5 ")


def wallet_size():
    if int(wallet) > 5:
        return True
    else:
        print("Get money")

def auth (name):
    if name in user['name']:
        print("Hello! ")
    


is_running = True

is_registred = False

while is_running :
    user_choose = input("""
        a) 
        b) Register
        c) Auth
        q) Quit
        
    Answer : """).lower()

    if user_choose == "b":
        name = input("Enter your name  : ")
        name_lenght()

        age = input("Enter your age : ")
        how_old()
            
        wallet = input("How much money u have? : ")
        wallet_size()

        user = registration(name, age, wallet)
        users_base.append(user)
        print(users_base)


    if user_choose == "c":
        name = input("your name pls :")
        auth()