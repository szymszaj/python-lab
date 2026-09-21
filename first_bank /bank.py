from datetime import datetime

class KontoBankowe:
    def __init__(self, wlasciciel, saldo=0.0):
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        self.historia = []

    def wplata(self, kwota):
        if kwota <= 0:
            print("Kwota wpłaty musi być dodatnia.")
            return
        self.saldo += kwota
        self._zapisz_operacje("Wpłata", kwota)
        print(f"Wpłacono {kwota:.2f} zł. Nowe saldo: {self.saldo:.2f} zł")

    def wyplata(self, kwota):
        if kwota <= 0:
            print("Kwota wypłaty musi być dodatnia.")
            return
        if kwota > self.saldo:
            print("Brak wystarczających środków.")
            return
        self.saldo -= kwota
        self._zapisz_operacje("Wypłata", kwota)
        print(f"Wypłacono {kwota:.2f} zł. Nowe saldo: {self.saldo:.2f} zł")

    def oblicz_odsetki(self, oprocentowanie_roczne):
        """Przykład 'czystych obliczeń' - to jest domena Pythona."""
        odsetki = self.saldo * (oprocentowanie_roczne / 100)
        return round(odsetki, 2)

    def _zapisz_operacje(self, typ, kwota):
        wpis = {
            "typ": typ,
            "kwota": kwota,
            "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.historia.append(wpis)

    def pokaz_historie(self):
        if not self.historia:
            print("Brak operacji.")
            return
        print(f"\nHistoria operacji dla {self.wlasciciel}:")
        for wpis in self.historia:
            print(f"  [{wpis['data']}] {wpis['typ']}: {wpis['kwota']:.2f} zł")


def menu():
    konto = KontoBankowe("Jan Kowalski", saldo=1000.0)

    while True:
        print("\n--- APLIKACJA BANKOWA ---")
        print(f"Saldo: {konto.saldo:.2f} zł")
        print("1. Wpłata")
        print("2. Wypłata")
        print("3. Oblicz odsetki (roczne, 3%)")
        print("4. Historia operacji")
        print("5. Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            kwota = float(input("Podaj kwotę wpłaty: "))
            konto.wplata(kwota)
        elif wybor == "2":
            kwota = float(input("Podaj kwotę wypłaty: "))
            konto.wyplata(kwota)
        elif wybor == "3":
            odsetki = konto.oblicz_odsetki(3)
            print(f"Odsetki roczne przy 3%: {odsetki:.2f} zł")
        elif wybor == "4":
            konto.pokaz_historie()
        elif wybor == "5":
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidłowa opcja.")


if __name__ == "__main__":
    menu()