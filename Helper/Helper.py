# github.com/czakk; author: czak; date:05/11/2020
#Title: TD2 Helper;
#Description: Generator komend do symulatora TD2(td2.info.pl);version: 0.4;Last-Update: 13/11/2020;
def file_exist(file_path):
    """Sprawdza czy podany plik istnieje!"""
    try:
        x = open(file_path)
    except IOError:
        verify = "brak połączenia z plikiem "+file_path
        return verify
    else:
        verify = "zainicjowano plik "+file_path
        x.close()
        return verify

def display_veh(file_path):
    dir = open(file_path,"r")
    vehicles = dir.readlines()
    vehicles.pop(vehicles.index("Wagony\n"))
    for vehicle in vehicles:
         print(str(index)+".",vehicle,end="")
         index += 1
    return vehicles

def choice_veh(variable):
        vehicle = display_veh("squad.txt")
        while variable == "lista":
            index = int(get_params("\nPodaj konstrukcje z listy: ",1))
            if index < 0:
                print("Indeks nie może być mniejszy od 0!")
            else:
                try:
                    variable = vehicle[index]
                except ValueError:
                    print("Podana wartość nie jest liczbą!")
                except IndexError:
                    print("Nie mamy tego na liście")
        return variable
def display_hello():
    """Wyświetlanie wiadomości powitalnej"""
    print("""Witam w Generatorze Komend w symulatorze Train Driver 2\t
            Jest to wersja wczesna, błędy można zgłaszać na forum,github,dc:czak#4333\t\t
                Dziękuje za testowanie aplikacji\n""")
    print("Inicjacja pliku tekstowego:",file_exist("squad.txt"))
    print("Inicjacja pliku tekstowego:",file_exist("post.txt"),"\n")
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
    if len(parms[0]) != 0:parms[0] += "_"
    else:parms[0] = ""
    parms[1] = get_params("Podaj semafor pod którym ma pojawić się skład!: ",1)
    parms[2] = get_params("Podaj odległośc od semafora: ",1)
    parms[3] = get_params("Podaj ilość wagonów: ",1)
    parms[4] = get_params("Jaki typ pojazdu chcesz stworzyć? Jeżeli chcesz otworzyć listę pojazdów wpisz 'lista': ",1)
    if parms[4] == "lista":
       parms[4] = choice_veh(parms[4])
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
    parms = [1,2,3,4,5]
    display_hello()
    choice = menu()
    if choice == "1":
      parms = sq_generator(choice,parms)
    elif choice == "2":
        parms = kick_generator(choice,parms)
    cmd_generator(parms,choice)

def test(file_path):
    """Wczytuje liste pojazdów i przypisuje je do listy veh"""
    file = open(file_path,"r")
    vehicles = file.readlines()
    title = []
    def test2(list1,list2,name):
       try: 
           list1.append(list2.pop(list2.index(name+"\n")))
       except ValueError:
           print("nazwa",name,"nie istnieje")
    test2(title,vehicles,"Wagony")
    test2(title,vehicles,"Lokomotywy")
    test2(title,vehicles,"Obiekty gracza")
    veh = []
    for i in range (len(title)):
        veh.append([])
    for i in range(len(title)):
        for j in range(vehicles.index("end\n")):
            veh[i].append(vehicles[j].replace("\n",""))
        del vehicles[0:vehicles.index("end\n")+1]
    file.close()
    return veh,title

vehicles,titles = test("squad.txt")
for i in range(len(titles)):
    print("\n"+titles[i])
    for j in range(len(vehicles[i])):
        print(str(i)+"."+str(j),vehicles[i][j])
while True:
    x = get_params("Podaj pojazd który ciebie interesuje: ",1)
    try:
        print(vehicles[int(x[0])][int(x[1])])
        break
    except IndexError:
        print("Wybrana opcja nie istnieje")
    except ValueError:
        print("Wartość musi być liczbą")

#implementacja test1() do kodu głównego
#zrobienie coś z tytułami w funkcji test(1)