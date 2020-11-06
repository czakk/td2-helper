# github.com/czakk; author: czak; date:05/11/2020
#Title: TD2 Helper;
#Description: Generator komend do symulatora TD2(td2.info.pl);version: 0.1;Last-Update: 07/11/2020;

print("""Witam w Generatorze Komend w symulatorze Train Driver 2\t
            Jest to wersja wczesna, błędy można zgłaszać na forum,github,dc:czak#4333\t\t
                Dziękuje za testowanie aplikacji\n""")


menu_choice = None
player_name = None
reason = None

while menu_choice == None:
    while menu_choice != 0:
        print("""Wybierz opcję która cię interesuję:
                1.Generator składów
                2.Wyrzucenia Gracza
                3.Zamknięcie programu
                                    """)
        menu_choice = input("Podaj numer: ")
        if menu_choice:
            if menu_choice == "1":
                print("Witaj, w generatorze komeny do spawnów składów")
                distance = "1"
                #tu będzie pętla while sprawdzająca prawdziwość argumentów
            
                post = input("Podaj Posterunek na którym się znajdujesz (np.Ps,Tw): ") #Podajemy posterunek na którym się znajdujemy, ponieważ wymagane jest podanie również tego przy zdefiniowaniu konkretnego semafora
            
                sem = input("Podaj Posterunek na którym się znajdujesz (np.G2,A): ")
            
                distance = input("Podaj dystans od semafora. Standardowa wartość to '1': ")
            
                amount = input("Podaj ilość wagonów(min. 1): ")
            
                wagoons = input("Jaki model konstrukcyjny chcesz spawnować: ")
           
                print("Wygenerowana komenda:")
                print("\t/sp " +post.title()+ "_" +sem.title()+ ":" +distance, "n:" +amount+ "," +wagoons)
            elif menu_choice == "2":
                while reason or player_name == None:
                      player_name = input("Podaj nazwe gracza: ")
                      reason = input("Podaj powód: ")
                      if reason or player_name != None:
                        print("Wygenerowana komenda:")
                        print("/kick_player",player_name,reason)
                        break
                      else:continue;
        
            elif menu_choice == "3":break
            else:print("Wkrótce!\n");menu_choice = None;continue
        else:print("Nie podano opcji!");menu_choice = None;continue

           




#/sp A n:5,eaos;
# /sp [sygnalizator]:[odległość] [skład]
#/rmcar Ps_It2e
