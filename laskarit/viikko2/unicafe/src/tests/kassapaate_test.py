import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)
        self.kassa = Kassapaate()

    def test_kassan_alkusaldo_on_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisten_lounaiden_maara_on_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaiden_lounaiden_maara_on_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_syo_edullisesti_kateisella_toimii(self):
        raha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(raha, 60)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_syo_edullisesti_kateinen_ei_riita(self):
        raha = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(raha, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)


    def test_syo_maukkaasti_kateisella_toimii(self):
        raha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(raha, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)


    def test_syo_maukkaasti_kateinen_ei_riita(self):
        raha = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(raha, 300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_syo_edullisesti_kortilla_katetta_on(self):
        tulos = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(tulos, True)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kortti.saldo, 760)

    def test_syo_edullisesti_kortilla_kate_ei_riita(self):
        visa = Maksukortti(200)
        tulos = self.kassa.syo_edullisesti_kortilla(visa)
        self.assertEqual(tulos, False)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(visa.saldo, 200)

    def test_syo_maukkaasti_kortilla_katetta_on(self):
        tulos = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(tulos, True)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_kate_ei_riita(self):
        visa = Maksukortti(300)
        tulos = self.kassa.syo_maukkaasti_kortilla(visa)
        self.assertEqual(tulos, False)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(visa.saldo, 300)

    def test_kortin_lataus_toimii(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)
        self.assertEqual(self.kortti.saldo, 1500)

    def test_velaksi_lataus_ei_onnistu(self):
        tulos = self.kassa.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(tulos, None)




    


     




# Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva
#   rahamäärä kasvaa ladatulla summalla