import re


def user(email , login , password) :
    return {
        'email' : email ,
        'login' : login ,
        'password' : password
    }

def registrartion() :
    return []


def validation(email , login , password) :
    # email , login , password , *args = user.values()

    email_rules = {
        'email_validation' : re.search(r'[@.]' , email)
    }

    login_rules = {
        'login_uppercase' : login[0].isupper() ,
        'login_lenght' : len(login) < 2

    }

    password_rules = {
        'password_numbers' : re.search(r'[1-9]' , password) ,
        'password_lenght' : len(password) < 6 ,
        'password_uppercase' : re.search(r'[A-Z]', password) ,
        'password_lowercase' : re.search(r'[a-z]' , password) ,
        'password_special_symbols' : re.search(r'[!@#$%^&*()-_][}{};:<>?/,.`~]' , password)
    }

    if email_rules['email_validation'] or login_rules['login_lenght'] or login_rules['login_uppercase'] or password_rules['password_lenght'] or password_rules['password_lowercase'] or password_rules['password_numbers'] or password_rules['password_special_symbols'] or password_rules['password_uppercase'] :
        raise TypeError("Something went wrong")

    # arr.append(user)

    return True


users = []

is_running = True

while is_running:
    user_choose = input("""
    A) Registration
    B) Authorization
    """).lower()
    if user_choose == 'a' :
        email = input("Your email pls: ")
        
        login = input("Youe login pls: ")

        password = input("Youe password pls: ")

        validation(email , login , password)
        
        users = user(email, login, password)
        
        print(user)
       

