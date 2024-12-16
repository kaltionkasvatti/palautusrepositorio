from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from pelaaja import Pelaaja
from kayttoliittyma import(
    Pelaajat,
    check_siirto
)

class KPSpeli:
    def __init__(self, muoto):
        self.muodot = {
            "a": Pelaaja(Pelaajat.TOKA),
            "b": Tekoaly(),
            "c": TekoalyParannettu(10)
        }
        self.vastus = self.muodot[muoto]
    def pelaa(self):
        tuomari = Tuomari()
        pelaaja = Pelaaja(Pelaajat.EKA)

        ekan_siirto = pelaaja.anna_siirto()
        tokan_siirto = self.vastus.anna_siirto()

        while check_siirto(ekan_siirto) and check_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = pelaaja.anna_siirto()
            tokan_siirto = self.vastus.anna_siirto()

        print("Kiitos!")
        print(tuomari)