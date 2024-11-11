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

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaaminen_kun_ei_tilaa(self):
        self.varasto.lisaa_varastoon(12)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisaataan_negatiivinen(self):
        self.varasto.lisaa_varastoon(-4)

        #Vapaata tilaa ei pitäisi tulla lisää eli pysyy
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ota_varastosta_enemman_kuin_tilaa(self):
        saatu_maara = self.varasto.ota_varastosta(100)

        self.assertAlmostEqual(saatu_maara, 0)
        self.varasto.lisaa_varastoon(6)

        saatu_maara = self.varasto.ota_varastosta(100)

        self.assertAlmostEqual(saatu_maara, 6)

    def test_ota_varastosta_neg(self):
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_stringina(self):
        self.varasto.lisaa_varastoon(8)
        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")

    def test_konstruktori_alkusaldo_liikaa(self):
        varasto = Varasto(10, 24)
        self.assertAlmostEqual(varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(varasto.tilavuus, 10)

    def test_konstruktori_neg_tilavuus(self):
        varasto = Varasto(-2, 0)
        self.assertAlmostEqual(varasto.tilavuus, 0)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_alkusaldo_negatiivinen(self):
        varasto = Varasto(10, -6)
        self.assertAlmostEqual(varasto.paljonko_mahtuu(), 10)
        self.assertAlmostEqual(varasto.tilavuus, 10)
