import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_virheellinen_tilavuus(self):
        virhe_varasto = Varasto(-5)

        self.assertEqual(virhe_varasto.tilavuus, 0)

    def test_saldo_suurempi_kuin_tilavuus(self):
        virhe_varasto = Varasto(5, 10)

        self.assertEqual(virhe_varasto.saldo, virhe_varasto.tilavuus)

    def test_virheellinen_saldo(self):
        virhe_varasto = Varasto(5, -5)

        self.assertEqual(virhe_varasto.saldo, 0)
    
    def test_virheellinen_lisays(self):
        testisaldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, testisaldo)
    
    def test_lisaa_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(15)
        self.assertEqual(self.varasto.tilavuus, self.varasto.saldo)
    
    def test_ota_enemmän_kuin_on_tilaa(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.ota_varastosta(10), 5)
    
    def test_virheellinen_otto(self):
        self.assertEqual(self.varasto.ota_varastosta(-10), 0)
    
    
    def test_tulostus(self):
        print(self.varasto)