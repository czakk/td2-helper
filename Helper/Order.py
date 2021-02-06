from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class Order:
    def __init__(self, order):
        now = datetime.now()
        self.order_type = ""
        self.order_number: int = 0
        self.train_number: int = 0
        self.date = now.strftime("%d,%y")
        self.image = Image.open(order + ".JPG")
        self.fnt = ImageFont.truetype("C:\WINDOWS\FONTS\ARIAL.TTF", 40)
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
        self.draw.text((1080, 100), self.order_number, font=self.fnt, fill=(0, 0, 0))

        # get and print Train Number
        self.train_number = self.get_args("Podaj numer pociągu: ", True)
        self.draw.text((467, 220), self.train_number, font=self.fnt, fill=(0, 0, 0))

        # print date
        self.draw.text((960, 220), self.date[:2], font=self.fnt, fill=(0, 0, 0))
        self.draw.text((1248, 220), self.date[3:], font=self.fnt, fill=(0, 0, 0))


class Order_N(Order):

    def plot_1(self):
        start = self.get_args("Tor zamknięty od: ", True)
        self.draw.text((367, 312), start, font=self.fnt, fill=(0, 0, 0))

        end = self.get_args("Do: ", True)
        self.draw.text((850, 312), end, font=self.fnt, fill=(0, 0, 0))

        track_num = self.get_args("Tor numer: ", True)
        self.draw.text((486, 380), track_num, font=self.fnt, fill=(0, 0, 0))

        drive_allow = self.get_args("Ruch prowadzony na torze nr: ", True)
        self.draw.text((1143, 446), drive_allow, font=self.fnt, fill=(0, 0, 0))

    def finish_order(self):

        self.get_information()
        used_plots = []

        while True:
            print("""
            1. Tor Zamknięty Od-Do
            8. Koniec tworzenia rozkazu""")
            plot = self.get_args("Podaj którą działka jesteś zainteresowany: ", True)
            if plot in used_plots:
                print("Działka została już użyta")
                continue
            else:
                used_plots.append(plot)
            if plot == "1":
                self.plot_1()
            elif plot == "8":
                self.image.show()
                self.image.save("Orders/" + self.train_number + "." + self.order_number + "." + self.date[:2] + ".jpg")
                break
            else:
                print("Podaj 1")


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


main()
