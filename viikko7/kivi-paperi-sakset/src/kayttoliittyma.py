class Pelaajat:
    EKA = 1
    TOKA = 2

def aloitus():
    print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
    return input()

def check_siirto(siirto):
    return siirto == "k" or siirto == "p" or siirto == "s"

def pelataanko(vastaus: str):
    return vastaus.endswith("a") or vastaus.endswith("b") or vastaus.endswith("c")