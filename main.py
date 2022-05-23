liczba_pracownikow = int(input())


class Pracownik:
    def __init__(self,imie,wynagrodzenie_brutto):
        
        self.imie = imie
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.skladka = round(self.wynagrodzenie_brutto*0.0976,2) + round(self.wynagrodzenie_brutto*0.015,2) + round(self.wynagrodzenie_brutto*0.0245,2)
        self.ubezpieczenie = round((self.wynagrodzenie_brutto - self.skladka)*0.09,2)
        self.podatek = round((round((round(self.wynagrodzenie_brutto-111.25 - self.skladka,2))*0.18,2)-46.33) - round((round(self.wynagrodzenie_brutto-self.skladka,2))*0.0775,2),0)
        self.wyplata = round(self.wynagrodzenie_brutto - self.skladka - self.ubezpieczenie - self.podatek,2)
        self.koszt_pracodawcy = round(self.wynagrodzenie_brutto*0.0976,2) + round(self.wynagrodzenie_brutto*0.065,2) + round(self.wynagrodzenie_brutto*0.0193,2) + round(self.wynagrodzenie_brutto*0.0245,2) + round(self.wynagrodzenie_brutto*0.001,2)

    def __repr__(self):
        #return "{} {}".format{self.imie:.2f}..
        return f"{self.imie} {self.wyplata:.2f} {self.koszt_pracodawcy:.2f} {self.wynagrodzenie_brutto+self.koszt_pracodawcy:.2f}"
    
    def koszt_ostateczny(self):
        return self.wynagrodzenie_brutto + self.koszt_pracodawcy


dane_pracownikow = []
laczny_koszt = 0

for pracownik in range(liczba_pracownikow):
    dane_wejscowe = input()
    dane_pracownikow.append(dane_wejscowe)

for dane in dane_pracownikow:
    imie = dane.split(' ')[0]
    wynagrodzenie = int(dane.split(' ')[1])
    pracownik = Pracownik(imie,wynagrodzenie)
    print(pracownik)
    laczny_koszt+=pracownik.koszt_ostateczny()


print(f"{laczny_koszt:.2f}")