# TD2 Helper
Aplikacja stworzona dla graczy Symulatora [Train Driver 2](https://td2.info.pl/), która ma na celu ułatwić rozgrywkę poprzez Generator Komend lub Rozkazów Pisemnych (wkrótce). 
## Co aktualnie oferuje Aplikacja?
- Generator tworzenia pojazdów - Kiedy gracz prosi nas o stworzenie np. 5 węglarek pod semaforem C wystarczy, że użyjemy  naszego **Generatora**, podamy odpowiednie parametry a w wyniku otrzymamy komendę gotowa do wklejenia na chat gry
- Generator /kick_driver - Komenda pozwalająca wyrzucić nieodpowiedniego gracza z nasej scenerii
- Generator rozkazów pisemnych w wersji graficznej
- Historię pięciu ostatnich komend - Wyświetla pięć ostatnio utworzonych komend
- Dwa modyfikowalne pliki tekstowe dzięki którym możemy szybciej i wygodniej tworzyć obiekty
## O co chodzi z modyfikowalnymi plikami?
**Przykład 1**

![N|Solid](https://i.imgur.com/lnLbAdT.png)
![N|Solid](https://i.imgur.com/YyCjewi.png)

**Przykład 2**

![N|Solid](https://i.imgur.com/46bYOol.png)
![N|Solid](https://i.imgur.com/U7DaLWs.png)

| Znacznik | Wytłumaczenie |
| ------ | ------ |
| < | Odpowiada za zaznaczenie początku wyróżnionej kategorii w przypadku wyżej było to "Przykladowe Obiekty", lecz nazwa może być dowolna. Wymagane jest użycie chociaż jednego owego znacznika |
| > | Stawiany przy obiekcie **PO SPACJI** pomaga nam opisać obiekt po lewej stronie znacznika. Ważne jest odpowiednie umiejscowienie znacznika, ponieważ musi być on poprzedzony spacją. Również po wstawieniu go musimy użyć spacji (np. Grafitti > Wagon pasazerski z Grafitti). Korzystanie z tego nie jest wymagane
| end | Znacznik ten określa w którym miejscu chcemy zakończyć nasza kategorię. Zaleca się uzywanie raz na każdą kategorię |
## Instalacja
Instalacja odbywa się poprzez **Instalator** (link). Do poprawnego działania potrzebujemy modułu Pillow
