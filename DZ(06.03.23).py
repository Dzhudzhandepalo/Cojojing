empty_array = []

empty_string = ""

register_data = {
    "data1" : empty_string
}


register_data['login'] = input("Your login sir :")

register_data['password'] = input("And password of course, Sir :")

if len(register_data["login"]) < 5 and len(register_data["password"]) < 10 :
    print("Error")
    print("Error")
