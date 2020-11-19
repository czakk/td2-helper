#   github.com/czakk/td2-helper; author: czak; date:05/11/2020
#   Title: TD2 Helper;
#   Description: Generator komend do symulatora TD2(td2.info.pl);version: 0.5;Last-Update: 19/11/2020 by czak;

class File_test(object):
    """Testuje pliki czy posiadają poprawne parametry"""
    
    def __init__(self,file):
        self.file = file
        self.__error = None
        try:
            self.file = open(file,"r")
            self.file_name = file
        except IOError as e:
            self.__error = e

    def file_exist(self):
        if self.__error:
            print("Plik", self.file_name, "nie może zostać zainicjowany. Kod błędu",self.__error+"\n")
            self.file = 0
        else:
            print("Plik", self.file_name,"został zainicjowany \n")
       

    def list_display(self):
        """Usuwa wszystko po znaku '-' we wczytanym pliku"""
        if self.file == 0:
            print("Wystąpił problem z plikiem",self.file,"kod błędu",self.error)
        else:
            display_list = self.file.readlines()
            
            for i in range(len(display_list)):
                display_list.insert(i,display_list[i].replace("\n",""))
                display_list.pop(i+1)
            
            choice_list = display_list[:]
            
            for i in range(len(choice_list)):
                try:
                    choice_list.insert(i,choice_list[i][:choice_list[i].index(">")-1])
                    choice_list.pop(i+1)
                except:continue
            return display_list,choice_list

def load_vehicle(file_path):
    """Wczytuje liste pojazdów i przypisuje je do listy veh"""
    file = File_test("squad.txt")
    vehicle_d,vehicle_c = file.list_display()
    title = []
    def titles(list1,list2):
       """Usuwa title z pliku squad.txt"""
       for i in list1:
          if i[0] == "<":
              list2.append(i[1:])
              list1.pop(list1.index(i))
    titles(vehicle_c,title)
    veh = []
    for i in range (len(title)):
        veh.append([])
    for i in range(len(title)):
        for j in range(vehicle_c.index("end")):
            veh[i].append(vehicle_c[j].replace("\n",""))
        del vehicle_c[0:vehicle_c.index("end")+1]
    file.file.close()
    return veh,title

#def load_post(file_path):
#    """Funkcja załadowuje posterunki z pliku podanego w argumencie, tworzy kopie listy posterunków i w tej kopii tworzy posterunki bez cały nazw np. Ps zamiast Ps - Piaskowo"""
#    file = open(file_path, "r")
#    post_todisplay = file.readlines()
#    for i in range(len(post_todisplay)):
#            post_todisplay.insert(i,post_todisplay[i].replace("\n",""))
#            post_todisplay.pop(i+1)
#    post_tochoice = post_todisplay[:]
#    for i in range(len(post_tochoice)):
#        post_tochoice.insert(i,post_tochoice[i][:post_tochoice[i].index("-")-1])
#        post_tochoice.pop(i+1)
#    return post_todisplay,post_tochoice

def choice_post():
     file = File_test("post.txt")
     display,choice = file.list_display()
     for i in range(len(display)):
        print(str(i)+".",display[i])
     while True:
        x = get_params("Który posterunek wybierasz?: ",1)
        try:
            return(choice[int(x)])
            break
        except IndexError:
            print("Wybrana opcja nie istnieje")
        except ValueError:
            print("Wartośc musi być liczbą")

def choice_vehicle():
    """Wyświetla i zwraca pojazd z pliku squad.txt"""
    vehicles,titles = load_vehicle("squad.txt")
    for i in range(len(titles)):
        print("\n"+titles[i])
        for j in range(len(vehicles[i])):
            print(str(i)+"."+str(j),vehicles[i][j])
    while True:
        x = get_params("Podaj pojazd który ciebie interesuje: ",1)
        try:
            return(vehicles[int(x[:x.index(".")])][int(x[x.index(".")+1:])])
            break
        except IndexError:
            print("Wybrana opcja nie istnieje")
        except ValueError:
            print("Wartośc nie jest liczbą lub zabrakło '.' pomiędzy liczbami.")

def display_hello():
    """Wyświetlanie wiadomości powitalnej"""
    f1 = File_test("squad.txt")
    f2 = File_test("post.txt")
    print("""Witam w Generatorze Komend w symulatorze Train Driver 2\t
            Jest to wersja wczesna, błędy można zgłaszać na forum,github,dc:czak#4333\t\t
                Dziękuje za testowanie aplikacji\n""")
    f1.file_exist()
    f2.file_exist()

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

def sq_generator(parms):
    """Generuje komendy do spwanowania składu, zwraca: """
    parms[0] = get_params("Podaj posterunek na którym się znajdujesz. Niektóre scenerie tego nie wymagają! (Cis). By otworzyc listę posterunków wpisz 'lista': ",0)
    if parms[0] == "lista":
        parms[0] = choice_post()
    if len(parms[0]) != 0:parms[0] += "_"
    else:parms[0] = ""
    parms[1] = get_params("Podaj semafor pod którym ma pojawić się skład!: ",1)
    parms[2] = get_params("Podaj odległośc od semafora: ",1)
    parms[3] = get_params("Podaj ilość wagonów: ",1)
    parms[4] = get_params("Jaki typ pojazdu chcesz stworzyć? Jeżeli chcesz otworzyć listę pojazdów wpisz 'lista': ",1)
    if parms[4] == "lista":
        parms[4] = choice_vehicle()

    while True:
        choice = get_params("Czy chcesz coś dodać do obecnego składu? t/n: ",1)
        if choice.lower() == "t":
            for i in range(2):
                parms[5] = ""
                if i == 0:
                    parms[5] = get_params("Podaj ilość wagonów: ",1)
                    parms[4] += ";n:"+parms[5]+","
                else:
                    parms[5] = get_params("Jaki typ pojazdu chcesz stworzyć? Jeżeli chcesz otworzyć listę pojazdów wpisz 'lista': ",1)
                    if parms[5] == "lista":
                        parms[5] = choice_vehicle()
                    parms[4] += parms[5]
        elif choice.lower() == "n":
            break
    return parms

def kick_generator(parms):
    """Generuje komende która wyrzuca gracza"""
    parms[0] = get_params("Podaj nick lub indetyfikator gracza: ",1)
    parms[1] = get_params("Podaj powód (niewymagane): ",0)
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
    parms = [1,2,3,4,5,""]
    display_hello()
    choice = menu()
    if choice == "1":
      parms = sq_generator(parms)
    elif choice == "2":
       parms = kick_generator(parms)
    cmd_generator(parms,choice)
        
main()

#input("\nNaciśnij enter aby zakończyć!\n")
#zrobienie coś z tytułami w funkcji test(1)