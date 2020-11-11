# github.com/czakk; author: czak; date:05/11/2020
#Title: TD2 Helper;
#Description: Generator komend do symulatora TD2(td2.info.pl);version: 0.3;Last-Update: 11/11/2020;

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

def sq_generator(choice,parms):
    """Generuje komendy do spwanowania składu, zwraca: """
    parms[0] = get_params("Podaj posterunek na którym się znajdujesz. Niektóre scenerie tego nie wymagają! (Cis): ",0)
    if len(parms[0]) != 0:
        parms[0] += "_"
    else:parms[0] = ""
    parms[1] = get_params("Podaj semafor pod którym ma pojawić się skład!: ",1)
    parms[2] = get_params("Podaj odległośc od semafora: ",1)
    parms[3] = get_params("Podaj ilość wagonów: ",1)
    parms[4] = get_params("Jaki typ pojazdu chcesz stworzyć?: ",1)
    return parms

def kick_generator(choice,parms):
    """Generuje komende która wyrzuca gracza"""
    parms[0] = get_params("Podaj nick lub indetyfikator gracza: ",1)
    parms[1] = get_params("Podaj powód (niewymagane)",0)
    return parms
def cmd_generator(parms,choice):
    """Generuje komendy"""
    print("\nWygenerowana komenda")
    if choice == "1":
        print("\t/sp " +parms[0].title()+parms[1].title()+ ":" +parms[2], "n:" +parms[3]+ "," +parms[4])
    elif choice == "2":
        print("\t/kick_driver",parms[0],parms[1])
    else:print("Wystąpił Błąd")
def main():
    """Główna funkcja programu"""
    #post,sem,dist,amount,wag_typ = "","","","",""
    parms = [1,2,3,4,5]
    display_hello()
    choice = menu()
    if choice == "1":
      parms = sq_generator(choice,parms)
    elif choice == "2":
        parms = kick_generator(choice,parms)
    cmd_generator(parms,choice)


main()