from kayttoliittyma import Pelaajat

class Pelaaja:
    def __init__(self, pelaaja):
        self.siirrot = {
        Pelaajat.EKA: "Ensimmäisen pelaajan siirto: ",
        Pelaajat.TOKA: "Toisen pelaajan siirto: "
        }
        self.pelaaja = self.siirrot[pelaaja]
    def anna_siirto(self):
        return input(self.pelaaja)