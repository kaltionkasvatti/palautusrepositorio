from kps_peli import KPSpeli
import kayttoliittyma as ui


def main():
    while True:

        vastaus = ui.aloitus()
        
        if ui.pelataanko(vastaus):
            peli = KPSpeli(vastaus[-1])
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
