def registration(email, password) :
    return {
        'email' : email ,
        'password' : password
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
        password = input("Password (- more than 6 symbols, must contain upper and lower-case letters, must contain number , or symbols as : “@” , “!” , etc.)")
        
        users = registration(email, password)

        print(users)

