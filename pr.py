# Registration
# 1) Get userName
# 2) Email
# 3) Password
# 4) Confirm password
# check -> True / False
# get value to check and statement for requirements

user_name = input("Get your name : ")
email = input("Get your email : ")
password = input("Get your password : ")
is_checked = None
#def name_validation ():

def password_validation(parameters):
    lenght , symbols , register , is_checked = parameters
    if len(password) <= 5 :
        password = False
    else: print(password_validation(True))

    if symbols != ("! , @ , # , $ , % , ^ , & , * , ( , ) ") :
        password = False
    else: print(password_validation(True))

    #if register 



def registration (options ):
    user_name  , email , password , is_checked = options
    print(user_name)
    print(email)
    print(password)

    print(is_checked)

registration([user_name , email , password , is_checked])