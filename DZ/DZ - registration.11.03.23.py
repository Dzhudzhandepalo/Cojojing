import re


def password_numbers(password) :
    if not re.search(r'[1-9]' , password) :
        raise TypeError("Must have number! ")

def password_lenght(password) :
    if len(password) < 6 :
        raise TypeError("Password must have more than 6 symbols! ")


def uppercase(password) :
    if not re.search(r'[A-Z]', password) :
        raise TypeError("Must have uppercase letter! ")


def lowercase(password) :
    if not re.search(r'[a-z]' , password) :
        raise TypeError("Must have lowercase letter! ")


def special_symbols_password(password) :
    if not re.search(r'[!@#$%^&*()-_][}{};:<>?/,.`~]' , password) :
        raise TypeError("Must have special symbols! ")


def email_validation(email) :
    if not re.search(r'[@.]' , email) :
        raise TypeError("Must have @ and . ")


def login_uppercase(login) :
    if not login[0].isupper() : 
        raise TypeError("Login starts from uppercase! ")

def login_lenght(login) :
    if len(login) < 2 :
        raise TypeError("Must be more than 2 symbols! ")

def registration(email, password , login) :
    return {
        'email' : email ,
        'password' : password ,
        'login' : login
    }


users = []

current_user = {}

current_user = False

is_running = True

while is_running:
    user_choose = input("""
    A) Registration
    B) Authorization
    """).lower()
    if user_choose == 'a' :
        email = input("Your email pls: ")
        email_validation(email)

        login = input("Choose your login: ")
        login_uppercase(login)
        login_lenght(login)


        password = input("Password (- more than 6 symbols, must contain upper and lower-case letters, must contain number , or symbols as : “@” , “!” , etc.)") 
        uppercase(password)
        lowercase(password)
        password_lenght(password)
        password_numbers(password)
        special_symbols_password(password)

        users = registration(email, password , login)

        print(users)

