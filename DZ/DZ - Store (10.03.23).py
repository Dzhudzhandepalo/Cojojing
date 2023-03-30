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
    for users in list_of_users :
        if login in users["login"]:
            password = input("Your password pls: ")
        

            if password == users["password"]:
                return [users, True]
            else :
                print("Wrong password")

def get_balance (wallet) :
    print("You have in your wallet: ", wallet['balance'])


def replenishment (wallet) :
    card_number = input("Card number (15 numbers) : ")
    card_number_validation(card_number)

    card_date = input("Card date (must include '/' ) : ")
    card_date_validation(card_date)

    card_cvv = input("Card CVV (3 numbers) : ")
    card_cvv_validation(card_cvv)

    money = input("How much money do you want to sent? : ")

    wallet['balance'] = int(wallet['balance']) + int(money)
    print(f"Thank you, now you have ", wallet['balance'] )


def card_number_validation(card_number) :
    if len(card_number) < 15 or len(card_number) > 15 :
        raise TypeError("Error, must be 15 numbers")

def card_date_validation(card_date) :
    if "/" not in card_date :
        raise TypeError("Error, example '12/12' ")
    
def card_cvv_validation(card_cvv) :
    if len(card_cvv) < 3 or len(card_cvv) > 3 :
        raise TypeError("Error, must be 3 numbers ")
    

def buy_sweets(target, list_of_products) :
    for product in list_of_products :
        if target.lower() == product['label'].lower() :
            current_user['balance'] = int(current_user['balance']) - int(product['price'])
    
    print(f"Thank you for purchase, your balance now is", current_user['balance'])


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

    
    elif user_choose == "b" :
        beauty_of_store (store)
        
        which_sweets = input("Choose sweets: ")

        buy_sweets(which_sweets, store)
    

    elif user_choose == "c" :
        login = input("Choose and remember your login : ")
        password = input("Choose and remember your password : ")
        user = registration(login , password)

        users.append(user)

        print(users)
    

    elif user_choose == "d" :
        login = input("Enter your login : ")

        resultation = auth(login, users)
        current_user, is_registred = resultation

        print(current_user)
        print(is_registred)


    elif user_choose == "f" :
        if not is_registred :
            print("You not registred")
            continue
        
        user_choose = input("""
        1)Get balance
        2)Replenishment by card
        """)
        if user_choose == "1" :
            if is_registred == True :
                get_balance(current_user)
            else :
                print("You must have an account")
        
        if user_choose == "2" :
            replenishment(current_user)
    
    
    
    elif user_choose == "q" :
        result = is_exit()
        if result == "y" :
            is_running = False


