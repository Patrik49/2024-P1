max_bodov = 30

#funkcia na ziskania validneho poctu bodov
def ziskaj_pocet_bodov():
    while True: # nekonecny cyklus
        try: 
            pocet_bodov =int(input(f"zadaj pocet bodov (0-{max_bodov})"))
            if 0 <= pocet_bodov <= max_bodov:
                return pocet_bodov
            else:
                print(f"pocet bodov musi byt v rozsahu 0 - {max_bodov}")
        except ValueError:
            print("cele zle")
            
            
def vypocitaj_percenta(pocet_bodov):
    return round ((pocet_bodov/max_bodov) *100 ,2)
            
            
def klasifikacia(percenta):
    if percenta >= 90:
        return '1'
    elif percenta >= 80:
        return '2'
    elif percenta >= 70:
        return '3'
    elif percenta >= 60:
        return '4'
    else: 
        return '5'


pocet_bodov = ziskaj_pocet_bodov()

percenta = vypocitaj_percenta(pocet_bodov)

hodnotenie = klasifikacia(percenta)

print(f"pocet bodov {pocet_bodov}, percenta {percenta}%")