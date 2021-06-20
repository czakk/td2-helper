#   github.com/czakk/td2-helper; author: czak; date:05/11/2020
#   Title: TD2 Helper;
#   Description: Generator komend do symulatora TD2(td2.info.pl);version: 0.9;Last-Update: 09/06/2021 by czak;
import sys


# import Order

class File(object):
    """Testuje pliki czy posiadają poprawne parametry"""

    def __init__(self, file):
        self.file_name = file
        self.__error = None
        try:
            self.file = open(file, "r")

        except IOError as e:
            self.__error = e

    def file_exist(self):
        if self.__error:
            print("Plik", self.file_name, "nie może zostać zainicjowany. Kod błędu", self.__error, "\n")
            return False

        def check_key(key):
            self.file.seek(0)
            if key not in self.file.read():
                print("W pliku", self.file_name, "brakuje znacznika", key)
                return False

        def compareKeyCount(key1: str, key2: str) -> bool:
            """Jeżeli liczba znacznika key1 nie jest równa key2 zwraca False"""
            self.file.seek(0)  # Ustawiamy 'czytnik' w pliku na początek
            text = self.file.read()
            if text.count(key1) != text.count(key2):
                print(f'W pliku {self.file_name} znaczników "{key1}" oraz "{key2}" musi być tyle samo!')
                return False

        if compareKeyCount('<', 'end') is False:
            return False

        if (check_key("<") is not False) and (check_key("end") is not False):
            print("Plik", self.file_name, "został zainicjowany \n")
        else:
            return False

        return True

    def display_list(self):
        """Praca z plikiem"""
        # wczytanie elementów, dodanie ich do odpowiednich list, usunięcie znacznika '\n' oraz '<
        elements = []
        objects = []
        # lista objects która będziemy wyswietlac z opisami
        display_objects = []
        self.file.seek(0)
        for i in self.file.readlines():
            if i[0] == "<":
                objects.append([i[1:].replace("\n", "")])
                continue
            elements.append(i.replace("\n", ""))

        for i in range(len(objects)):
            for j in elements:
                if j == "end":
                    display_objects.append(elements[:elements.index(j)])
                    del elements[:elements.index(j) + 1]
                    break
                else:
                    if ">" in j:
                        j = j[:j.index(">") - 1]
                    objects[i].append(j)
        return objects, display_objects

    def pick_object(self):
        pick, display = self.display_list()

        titles = [pick[i].pop(0) for i in range(len(pick))]

        for i in range(len(titles)):
            print("\n" + titles[i], "\n")
            for j in display[i]:
                index = display[i].index(j)
                print("[" + str(i) + "." + str(index) + "]", j)

        while True:
            choice = get_params("\nKtóry obiekt Ciebie interesuje?: ", 1)
            try:
                return pick[int(choice[:choice.index(".")])][int(choice[choice.index(".") + 1:])]
            except IndexError:
                print("Na wybranej pozycji nie znajduje się obiekt")
            except ValueError:
                print("Podana wartość jest nieprawidłowa")


def display_hello():
    """Wyświetlanie wiadomości powitalnej"""

    print("""Witam w Generatorze Komend w symulatorze Train Driver 2\t
            Jest to wersja wczesna, błędy można zgłaszać na forum,github,dc:czak#4333\t\t
                Dziękuje za testowanie aplikacji\n""")
    File("sklady_helper.txt").file_exist()
    File("posterunki_helper.txt").file_exist()


def menu():
    """Menu wyboru między opcjami programu, zwraca nr. opcji"""
    legal_choices = ("1", "2", "3", "4")
    user_choice = None
    while user_choice not in legal_choices:
        print("""Wybierz opcję która cię interesuję:
               1.Generator składów
               2.Wyrzucenia Gracza
               3.Historia Komend
               4.Zamknięcie programu
              """)
        user_choice = input("Która opcje wybierasz?: ")
        if user_choice not in legal_choices:
            print("Nie ma takiej opcji!")
    return user_choice


def get_params(question, req):
    """Zczytuje parametry i przypisuje je do zmiennej"""
    # req - czy wymagane jest podanie odpowiedzi
    if req == 0:
        variable = input(question)
    else:
        variable = ""
        while len(variable) == 0:
            variable = input(question)
    return variable


def sq_generator():
    parms = []
    """Generuje komendy do spwanowania składu, zwraca: """
    try:
        file1 = File("sklady_helper.txt")
        file2 = File("posterunki_helper.txt")
    except:
        return 0

    while True:
        parms.append(get_params(
            "Podaj posterunek na którym się znajdujesz. Niektóre scenerie tego nie wymagają! (Cis). By otworzyc listę "
            "posterunków wpisz 'lista': ",
            0))
        if parms[0] == "lista":
            if not file2.file_exist():
                print("Operacja nieudana")
            else:
                parms[0] = file2.pick_object()
                break
        else:
            break
    if len(parms[0]) != 0:
        parms[0] += "_"
    else:
        parms[0] = ""
    parms.append(get_params("Podaj semafor pod którym ma pojawić się skład!: ", 1))
    parms.append(get_params("Podaj odległośc od semafora: ", 1))
    parms.append(get_params("Podaj ilość wagonów: ", 1))
    while True:
        parms.append(get_params("Jaki typ pojazdu chcesz stworzyć? Jeżeli chcesz otworzyć listę pojazdów wpisz "
                                "'lista': ",
                                1))
        if parms[4] == "lista":
            if not file1.file_exist():
                print("Operacja nieudana")
            else:
                parms[4] = file1.pick_object()
                break
        else:
            break

    while True:
        choice = get_params("Czy chcesz coś dodać do obecnego składu? t/n: ", 1)
        if choice.lower() == "t":
            file3 = File("sklady_helper.txt")
            for i in range(2):
                parms.append("")
                if i == 0:
                    parms[5] = get_params("Podaj ilość wagonów: ", 1)
                    parms[4] += ";n:" + parms[5] + ","
                else:
                    while True:
                        parms[5] = get_params(
                            "Jaki typ pojazdu chcesz stworzyć? Jeżeli chcesz otworzyć listę pojazdów wpisz 'lista': ",
                            1)
                        if parms[5] == "lista":
                            if not file3.file_exist():
                                print("Operacja nieudana")
                            else:
                                parms[5] = file3.pick_object()
                                break
                        else:
                            break
                    parms[4] += parms[5]
        elif choice.lower() == "n":
            break
    return parms


def kick_generator():
    parms = ["", ""]
    """Generuje komende która wyrzuca gracza"""
    parms[0] = get_params("Podaj nick lub indetyfikator gracza: ", 1)
    parms[1] = get_params("Podaj powód (niewymagane): ", 0)
    return parms


def write_to_file(file, message):
    f = open(file, "a")
    f.write("\n" + message)
    f.close()


def cmd_generator(parms, choice):
    """Generuje komendy"""
    if choice in ("1", "2"):
        print("\nWygenerowana komenda")
    if choice == "1":
        command = "/sp " + parms[0].title() + parms[1].title() + ":" + parms[2] + " n:" + parms[3] + "," + parms[4]
        print("\t" + command)
        write_to_file("historia_helper.txt", repr(command))
        return command
    elif choice == "2":
        command = "/kick_driver " + parms[0] + " " + parms[1]
        print("\t" + command)
        write_to_file("historia_helper.txt", repr(command))
        return command
    elif choice == "3":
        return 0
    else:
        print("Wystąpił Błąd")


def history():
    try:
        f = open("historia_helper.txt", "r")
    except IOError:
        print("Brakuje pliku historia_helper.txt")
    else:
        print("\nHistoria 5 ostatnich komend:")
        pos = 5
        history = f.readlines()
        for i in range(len(history) - 5, len(history)):
            if len(history[i]) < 2:
                continue
            else:
                print(str(pos) + ".", history[i].replace("'", ""), end="")
                pos -= 1


def main():
    """Główna funkcja programu"""
    parms = []
    display_hello()
    while True:
        choice = menu()
        if choice == "1":
            parms = sq_generator()
        elif choice == "2":
            parms = kick_generator()
        elif choice == "3":
            history()
        elif choice == "4":
            print("Do następnego")
            sys.exit()
        cmd_generator(parms, choice)
        print("\n")


if __name__ == "__main__":
    main()
