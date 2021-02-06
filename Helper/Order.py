from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class Order:
    def __init__(self, order):
        now = datetime.now()
        self.order_number: int = 0
        self.train_number: int = 0
        self.date = now.strftime("%d,%y")
        self.image = Image.open("Order_template/" + order + ".JPG")
        self.fnt = ImageFont.truetype("C:\WINDOWS\FONTS\ARIAL.TTF", 48)
        self.draw = ImageDraw.Draw(self.image)

    @staticmethod
    def get_args(question: str, require: bool) -> str:
        """Function return user answer, in parameters we require question to insert in input and bool of answer is
        necessary """
        answer: str = ""
        if require:
            while answer == "":
                answer = input(question)
            return answer
        else:
            answer = input(question)
        return answer

    def get_information(self):
        # get and print Order Number
        self.order_number = self.get_args("Podaj numer rozkazu: ", True)
        self.draw_text((1080, 95), self.order_number)

        # get and print Train Number
        self.train_number = self.get_args("Podaj numer pociągu: ", True)
        self.draw_text((467, 215), self.train_number)

        # print date
        self.draw_text((960, 215), self.date[:2])
        self.draw_text((1248, 215), self.date[3:])

    def draw_text(self, coords: tuple, text: str):
        self.draw.text(coords, text, font=self.fnt, fill=(0, 0, 0))

    def draw_line(self, coords: tuple, width=5):
        self.draw.line(coords, fill=(0, 0, 0), width=width, joint="curve")


# noinspection PyTypeChecker
class Order_N(Order):

    def plot_1(self):
        start = self.get_args("Tor zamknięty od: ", True)
        self.draw_text((367, 300), start.title())

        end = self.get_args("Do: ", True)
        self.draw_text((850, 300), end.title())

        track_num = self.get_args("Tor numer: ", True)
        self.draw_text((486, 371), track_num)

        drive_allow = self.get_args("Ruch prowadzony na torze nr: ", True)
        self.draw_text((1143, 439), drive_allow)

    def plot_2(self):

        print("""
        Zezwolenie po:
        1. Sygnale "Nakaz Jazdy"
        2. Tylko tego rozkazu pisemnego
        """)
        choice = self.get_args("Co wybierasz?: ", True)
        if choice == "1":
            self.draw_line(((768, 628), (1285, 628)))
        elif choice == "2":
            self.draw_line(((819, 570), (1230, 570)))
        else:
            print("Prosze podać poprawną opcję")

        print("""
        Czy przy szlaku jest umieszczony semafor?:
        1. Tak
        2. Nie
        """)
        choice = self.get_args("Co wybierasz?: ", True)
        if choice == "1":
            # strike
            self.draw_line(((269, 1075), (1355, 1075)))
            self.draw_line(((262, 1150), (1355, 1150)))
            self.draw_line(((262, 1215), (1352, 1215)))

            # code
            print("""
            Semafor:
            1. Wyjazdowy
            2. Drogowskazowy
            3. Wjazdowy
            """)
            choice = self.get_args("Co wybierasz?: ", True)
            sem = self.get_args("Znacznik semafora?: ", True)
            if choice == "1":
                # Drogowskazowy
                self.draw_line(((262, 810), (1352, 810)))
                # Wjazdowy
                self.draw_line(((262, 810), (1352, 810)))

                # Semafor
                self.draw_text((600, 715), sem.title())

            elif choice == "2":
                # Wyjazdowy
                self.draw_line(((262, 752), (750, 752)))

                # Wjazdowy
                self.draw_line(((262, 873), (1352, 873)))

                # Semafor
                self.draw_text((670, 775), sem.title())

            elif choice == "3":
                # Wyjazdowy
                self.draw_line(((262, 752), (750, 752)))

                # Drogowskazowy
                self.draw_line(((262, 810), (1352, 810)))

                # Semafor
                self.draw_text((600, 835), sem.title())

            else:
                print("Prosze podać poprawną opcję")

            self.draw_text((720, 905), self.get_args("Wyjazd w kierunku?: ", True))
            coords = ((0, 0), (0, 0))
            print("""
            Wyjazd na szlak:
            1. Lewy
            2. Prawy
            """)
            choice = self.get_args("Co wybierasz?: ", True)
            if choice == "1":
                coords = ((657, 1020), (767, 1020))
            elif choice == "2":
                coords = ((548, 1020), (628, 1020))
            else:
                print("Prosze podać poprawną opcję")

            self.draw_line(coords)
            self.draw_text((1040, 985), self.get_args("Wyjazd na tor nr: ", True))
        elif choice == "2":
            # strike
            self.draw_line(((270, 692), (1205, 692)))
            self.draw_line(((262, 752), (750, 752)))
            self.draw_line(((262, 810), (1352, 810)))
            self.draw_line(((262, 873), (1352, 873)))
            self.draw_line(((280, 943), (1356, 943)))
            self.draw_line(((280, 1022), (1356, 1022)))

            # code
            self.draw_text((617, 1043), self.get_args("Wyjazd z toru nr: ", True))
            self.draw_text((889, 1113), self.get_args("Wyjazd w kierunku?: ", True))
            print("""
            Wyjazd na szlak:
            1. Lewy
            2. Prawy
            """)
            choice = self.get_args("Co wybierasz?: ", True)
            if choice == "1":
                coords = ((657, 1020), (767, 1020))
            elif choice == "2":
                coords = ((548, 1215), (628, 1215))
            else:
                print("Prosze podać poprawną opcję")

            self.draw_text((1092, 1180), self.get_args("Wjazd na tor nr?: ", True))

        else:
            print("Prosze podać poprawną opcję")

    def plot_3(self):
        coords1 = ((0, 0), (0, 0))
        coords2 = ((0, 0), (0, 0))
        print("""
        Przemieszczenie pociągu:
        1. Jazda
        2. Pchanie
        """)
        choice = self.get_args("Co wybierasz?: ", True)
        if choice == "1":
            coords1 = ((375, 1328), (580, 1328))
            coords2 = ((396, 1451), (583, 1451))
        elif choice == "2":
            coords1 = ((241, 1328), (339, 1328))
            coords2 = ((241, 1451), (362, 1451))
        else:
            print("Prosze podać poprawną opcję")

        self.draw_line(coords1)
        self.draw_line(coords2)

        self.draw_text((249, 1350), self.get_args("Jazda w kierunku?: ", True))

        self.draw_text((1065, 1350), self.get_args("do km?: ", True))

        self.draw_text((1223, 1414), self.get_args("Wracać będzie po lewym torze nr: ", True))

        self.draw_text((649, 1476), self.get_args("Najpózniej o godzinie (podaj samą godzine bez minut i sekund): ", True))
        self.draw_text((973, 1476), self.get_args("minucie: ", True))

    def finish_order(self):

        self.get_information()
        used_plots = []

        while True:
            print("""
            1. Tor Zamknięty Od-Do
            2. Wjazd na nieprawidłowy tor
            3. Pchanie pociągu
            8. Koniec tworzenia rozkazu
            """)
            plot = self.get_args("Podaj którą działka jesteś zainteresowany: ", True)
            if plot in used_plots:
                print("Działka została już użyta")
                continue
            else:
                used_plots.append(plot)
            if plot == "1":
                self.plot_1()

            elif plot == "2":
                self.plot_2()
            elif plot == "3":
                self.plot_3()
            elif plot == "8":
                self.image.show()
                self.image.save("Orders/" + "N" + self.train_number + "." + self.order_number + "." + self.date[:2] + ".jpg")
                break
            else:
                print("Brak wartości")


def choose_order():
    answer = ""
    while answer not in ("1", "2", "3"):
        print("""
        Który rozkaz wybierasz?
        1. N
        2. S
        3. O
        """)
        answer = input("Co wybierasz?: ")

    return answer


def main():
    order_type = choose_order()
    if order_type == "1":
        Order_N("N").finish_order()
    elif order_type == "2":
        pass
    elif order_type == "3":
        pass


main()
