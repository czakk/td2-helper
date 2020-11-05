
print("Witaj w Generatorze komend!")
print("Podaj co chcesz spawnować: .")
wagon = input("Podaj rodzaj wagonu: ")
sem = input("Podaj semafor pod którym spawnuja sie skład: ") #Podajemy Semafor
distance = input("Podaj odległość od semafora: ") #Odległość od semafora
amount = input("Podaj ilość wagonów: ") #Ilość wagonów

print("Komenda:\n/sp",sem+":"+distance,"n:"+amount+","+wagon)

#/sp A n:5,eaos;
# /sp [sygnalizator]:[odległość] [skład]
#/rmcar Ps_It2e

