def is_exit() :
    result = input("Do you want to quit from this life? y/n :")     # Футнкція для завершення програми 
    return result.lower()


def beauty_of_store (list_of_store) :
    for product in list_of_store :        # Функція сортування списку при запиті користувача
        print(product)


def registration (login , password , balance = 0) :      # Функція реєстрації, при реєстраціїї повинен бути баланс, але без поповнення він 0
    return {
        "login" : login ,
        "password" : password ,
        "balance" : balance
    }


def auth (login , list_of_users) :
    for user in list_of_users :
        print(user)


store = [
    {
        "label" : "kit-kat",
        "price" : "200"
    },
    {
        "label" : "milky way",
        "price" : "150"
    },
    {
        "label" : "snickers",
        "price" : "220"
    },
    {
        "label" : "twix",
        "price" : "190"
    },
    {
        "label" : "mars",
        "price" : "210"
    },
]


is_running = True


is_registred = False


users = [
    {
    "login" : "admin",
    "password" : "123456789",
    "balance" : "3000"
    }
]


current_user = {}


while is_running :
    user_choose = input("""
        a) Show products
        b) Buy product
        c) Registration
        d) Authorization
        f) Balance
        q) Exit
    Answer : """).lower()
    
    
    if user_choose == "a" :
        beauty_of_store(store)
    

    elif user_choose == "c" :
        login = input("Choose and remember your login : ")
        password = input("Choose and remember your password : ")
        user = registration(login , password)

        users.append(user)

        print(user)
    

    elif user_choose == "d" :
        login = input("Enter your login : ")


    
    
    elif user_choose == "q" :
        result = is_exit()
        if result == "y" :
            is_running = False


