# github.com/czakk; author: czak; date:05/11/2020
#Title: TD2 Helper;
#Description: Generator komend do symulatora TD2(td2.info.pl);version: 0.1;Last-Update: 11/11/2020;

#def end():
#    menu_choice = None

#print("""Witam w Generatorze Komend w symulatorze Train Driver 2\t
#            Jest to wersja wczesna, błędy można zgłaszać na forum,github,dc:czak#4333\t\t
#                Dziękuje za testowanie aplikacji\n""")


#menu_choice = None
#player_name = None
#reason = None

#while menu_choice == None:
#    while menu_choice != 0:
#        print("""Wybierz opcję która cię interesuję:
#                1.Generator składów
#                2.Wyrzucenia Gracza
#                3.Zamknięcie programu
#                                    """)
#        menu_choice = input("Podaj numer: ")
#        if menu_choice:
#            if menu_choice == "1":
#                print("Witaj, w generatorze komeny do spawnów składów")
#                distance = "1"
#                #tu będzie pętla while sprawdzająca prawdziwość argumentów
            
#                post = input("Podaj Posterunek na którym się znajdujesz (np.Ps,Tw): ") #Podajemy posterunek na którym się znajdujemy, ponieważ wymagane jest podanie również tego przy zdefiniowaniu konkretnego semafora
            
#                sem = input("Podaj Posterunek na którym się znajdujesz (np.G2,A): ")
            
#                distance = input("Podaj dystans od semafora. Standardowa wartość to '1': ")
            
#                amount = input("Podaj ilość wagonów(min. 1): ")
            
#                wagons = input("Jaki model konstrukcyjny chcesz spawnować: ")
           
#                print("Wygenerowana komenda:")
#                print("\t/sp " +post.title()+ "_" +sem.title()+ ":" +distance, "n:" +amount+ "," +wagoons)
#            elif menu_choice == "2":
#                while reason or player_name == None:
#                      player_name = input("Podaj nazwe gracza: ")
#                      reason = input("Podaj powód: ")
#                      if reason or player_name != None:
#                        print("Wygenerowana komenda:")
#                        print("/kick_player",player_name,reason)
#                        break
#                      else:continue;
        
#            elif menu_choice == "3":break
#            else:print("Wkrótce!\n");end()
#        else:print("Nie podano opcji!");end()

           




#/sp A n:5,eaos;
# /sp [sygnalizator]:[odległość] [skład]
#/rmcar Ps_It2e



def display_hello():
    """Wyświetlanie wiadomości powitalnej"""
    print("""Witam w Generatorze Komend w symulatorze Train Driver 2\t
            Jest to wersja wczesna, błędy można zgłaszać na forum,github,dc:czak#4333\t\t
                Dziękuje za testowanie aplikacji\n""")
def menu():
    """Menu wyboru między opcjami programu, zwraca nr. opcji"""
    legal_choices = ("1","2","3")
    user_choice = None
    while user_choice not in legal_choices:
          print("""Wybierz opcję która cię interesuję:
               1.Generator składów
               2.Wyrzucenia Gracza
               3.Zamknięcie programu
              """)
          user_choice = input("Która opcje wybierasz?: ")
          if user_choice not in legal_choices:
              print("Nie ma takiej opcji!")
    return user_choice


def get_params(question,req):
    """Zczytuje parametry i przypisuje je do zmiennej"""
    #req - czy wymagane jest podanie odpowiedzi
    if req == 0:
        variable = input(question)
    else:
        variable = ""
        while len(variable) == 0:
            variable = input(question)
    return variable

def sq_generator(choice):
    """Generuje komendy do spwanowania składu, zwraca: """
    post = get_params("Podaj posterunek na którym się znajdujesz. Niektóre scenerie tego nie wymagają! (Cis): ",0)
    if len(post) != 0:
        post += "_"
    sem = get_params("Podaj semafor pod którym ma pojawić się skład!: ",1)
    dist = get_params("Podaj odległośc od semafora: ",1)
    amount = get_params("Podaj ilość wagonów: ",1)
    wag_type = get_params("Jaki typ pojazdu chcesz stworzyć?: ",1)
    return post,sem,dist,amount,wag_type

def cmd_generator(choice,post,sem,dist,amount,wag_type):
    """Generuje komendy"""
    print("\nWygenerowana komenda")
    if choice == "1":
        print("\t/sp " +post.title()+sem.title()+ ":" +dist, "n:" +amount+ "," +wag_type)
    else:print("Wystąpił Błąd")
def main():
    """Główna funkcja programu"""
    post,sem,dist,amount,wag_typ = "","","","",""
    display_hello()
    choice = menu()
    if choice == "1":
      post,sem,dist,amount,wag_type = sq_generator(choice)
    cmd_generator(choice,post,sem,dist,amount,wag_type)




main()