import random
cheie = ""
lungime_cheie = 0
print("Cât de lungă vreți să fie cheia?")
limita_cheie = int(input("Cheia să fie de:"))
while lungime_cheie < limita_cheie:
    sector = [1,2,3,4]
    if random.choice(sector) == 1:
        sectiune1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        cheie = cheie + random.choice(sectiune1)
    elif random.choice(sector) == 2:
        sectiune2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        cheie = cheie + random.choice(sectiune2)
    elif random.choice(sector) == 3:
        sectiune3 = ["1","2","3","4","5","6","7","8","9","0"]
        cheie = cheie + random.choice(sectiune3)
    else:
        sectiune4 = ["!","@","#","$","%","&","*","?",";"]
        cheie = cheie + random.choice(sectiune4)
    lungime_cheie = lungime_cheie + 1
print("")
print("Cheia este:", cheie)
