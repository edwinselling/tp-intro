import random
kort1 = random.randint(1, 13)
kort2 = random.randint(1, 13)
print(f"Din giv är {kort1} och {kort2}, vilket ger totalen {kort1 + kort2}")
if kort1 + kort2 == 21:
    print("blackjack")
else:
    hus1 = random.randint(1,13)
    hus2 = random.randint(1,13)
    print(f"huset drar {hus1} och {hus2}, vilket ger totalen {hus1 + hus2}")
    
    stanna = "n"
    summa = kort1 + kort2
    while stanna.lower() == "n":
        print(f"Din totala summar är {summa}")

        stanna = input("stanna [j/n]")
        if stanna.lower() == "j":
            print(f"du stannar på {summa}")
            break
        elif summa == 21:
            print("blackjack")
            break
        elif summa == 21:
            print("du blev tjock, unlucky")
            break
        else:
            summa += random.randint(1, 13)

            huset = hus1 + hus2
            if summa < 21:
            while huset < 17:
                huset += random.randint(1, 13)
                print(f"huset har {huset}")

            if huset == 21 or huset > summa and huset < 21:
                print("dina drömar krossas av huset!")
            elif huset == summa:
                print("lika, try again")
            else:
                print("snyggt jobbat du vinner")

