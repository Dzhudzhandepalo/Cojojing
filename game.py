from random import randint

user = {
    "hp" : 100 ,
    "attack" : 10 ,
    "mana" : 50
}

def monster_finding():
    which_monster = randint(1, 3)

    print(which_monster)
    


monsters = [
    {
    "monster_id" : 1 ,
    "monster_name" : "spider",
    "hp" : 20 ,
    "attack" : 5 ,
    "mana" : 0
    } ,
    {
    "monster_id" : 2 ,
    "monster_name" : "ant",
    "hp" : 5 ,
    "attack" : 1 ,
    "mana" : 0
    } ,
    {
    "monster_id" : 3 ,
    "monster_name" : "titan",
    "hp" : 200 ,
    "attack" : 20 ,
    "mana" : 10
    }
]
# monsters['monster_id'] = monsters['monster_name']



is_running = True

while is_running :
    user_choose = input("""
        a) Find monster
        b) Attack
        c) Statistics
    Answer :  """).lower()

    if user_choose == "a" :
        result = monster_finding
        
