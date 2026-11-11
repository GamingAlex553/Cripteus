def gen_rondom():
    import random
    key = ""
    key_length = 0
    print("How long do you want the key to be?")
    key_caracter_limit = int(input("The key should have a character number of:"))
    while key_length < key_caracter_limit:
        sector = [1,2,3,4]
        if random.choice(sector) == 1:
            section1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            key = key + random.choice(section1)
        elif random.choice(sector) == 2:
            section2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            key = key + random.choice(section2)
        elif random.choice(sector) == 3:
            section3 = ["1","2","3","4","5","6","7","8","9","0"]
            key = key + random.choice(section3)
        else:
            section4 = ["!","@","#","$","%","&","*","?",";"]
            key = key + random.choice(section4)
        key_length = key_length + 1
    print("")
    print("The key is:", key)