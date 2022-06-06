from ClasePalindromo import Palindromo
import unittest


class TestPalindromo(unittest.TestCase):
    __palindromos = None

    def setUp(self):
        self.__palindromosOK = Palindromo("anana")
        self.__palindromosNOOK = Palindromo("casa")
    def test_PalindromosOK(self):
            self.assertTrue(self.__palindromosOK.esPalindromo(), True)

    def test_PalindromoNOOK(self):
        self.assertTrue(self.__palindromosNOOK.esPalindromo(), False)
