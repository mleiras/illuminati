# -*- coding: utf-8 -*-
import unittest
from IlluminatiEngine import IlluminatiEngine

class TestEngine(unittest.TestCase):
    
    def setUp(self):
        self.t1 = IlluminatiEngine()
        self.t1.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex1.ill")
        self.t1.resolve()
        
        self.t2 = IlluminatiEngine()
        self.t2.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex2.ill")
        self.t2.resolve()
        
        self.t3 = IlluminatiEngine()
        self.t3.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex3.ill")
        self.t3.resolve()
        
        self.t4 = IlluminatiEngine()
        self.t4.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex4.ill")
        self.t4.resolve()
    
        self.t5 = IlluminatiEngine()
        self.t5.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex5.ill")
        self.t5.resolve()

        self.t6 = IlluminatiEngine()
        self.t6.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex6.ill")
        self.t6.resolve()

        self.t7 = IlluminatiEngine()
        self.t7.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex7.ill")
        self.t7.resolve()

        self.t8 = IlluminatiEngine()
        self.t8.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex8.ill")
        self.t8.resolve()

        self.t9 = IlluminatiEngine()
        self.t9.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex9.ill")
        self.t9.resolve()

        self.t10 = IlluminatiEngine()
        self.t10.ler_tabuleiro_ficheiro("./exemplos_puzzles/ex10.ill")
        self.t10.resolve()

        
    def testTabuleiro(self):
        self.assertTrue(self.verify_lights(self.t1.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t2.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t3.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t4.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t5.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t6.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t7.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t8.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t9.gettabuleiro()))
        self.assertTrue(self.verify_lights(self.t10.gettabuleiro()))
        self.assertEqual(self.t1.gettabuleiro(), [['o', '@', 'x', '@', 'o', '0', 'o', '@', 'o', 'o'], ['0', '2', '@', 'o', 'o', 'o', 'o', 'o', '2', '@'], ['o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', '@', '2'], ['o', '@', '1', 'o', 'o', '@', '2', 'o', 'o', 'o'], ['@', 'o', 'o', 'x', '@', 'x', '@', 'o', '1', '@'], ['o', '0', 'o', '@', 'x', '@', '2', 'o', 'o', 'o'], ['o', 'o', '@', '3', '@', 'o', 'o', 'x', 'o', 'o'], ['x', 'o', 'o', 'o', 'o', 'o', '@', '3', '@', 'o'], ['@', '2', 'o', 'o', 'o', 'o', 'o', '@', '2', 'x'], ['o', '@', 'o', 'o', 'x', 'o', 'o', 'x', 'o', '@']])
        self.assertEqual(self.t2.gettabuleiro(), [['o', 'x', 'o', '@', '2', '@'], ['o', '@', 'o', 'o', 'o', 'o'], ['o', 'o', '0', 'x', '@', 'o'], ['o', 'o', '0', '0', 'o', 'o'], ['@', 'o', 'o', 'o', 'o', 'o'], ['o', '0', 'o', '@', '1', 'o']])
        self.assertEqual(self.t3.gettabuleiro(), [['x', 'o', '@', 'x', 'o', '@', '1', 'o', '@', 'x'], ['o', 'o', '2', '@', 'o', 'o', 'o', 'o', '1', 'o'], ['o', '@', '1', 'x', 'o', 'o', '@', 'o', 'o', 'o'], ['@', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', '@'], ['2', 'o', 'x', '@', 'o', 'o', '1', '@', 'o', 'o'], ['@', 'o', 'o', '3', '@', 'o', 'o', '1', 'o', 'x'], ['o', 'o', 'o', '@', 'o', 'o', 'o', '1', '@', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'x', 'x', 'o', 'o'], ['o', '0', 'o', 'o', 'o', 'o', '@', 'x', 'o', '@'], ['x', 'o', '@', 'x', 'o', 'o', 'x', '@', 'o', '1']])
        self.assertEqual(self.t4.gettabuleiro(), [['x', '0', 'o', '1', 'x', 'o', '@', 'o', 'o', 'o'], ['x', 'o', 'o', '@', '1', 'o', 'o', '0', 'o', '@'], ['o', '@', 'o', 'o', 'o', 'o', 'x', 'x', 'x', 'o'], ['0', 'o', '@', 'o', '1', '@', 'o', '1', '@', 'o'], ['1', 'x', 'o', '0', 'x', 'o', '@', 'o', 'o', 'o'], ['@', 'o', 'o', 'o', 'o', 'x', '1', 'o', 'x', 'x'], ['o', '@', 'x', 'o', '@', '1', 'o', 'o', 'o', 'x'], ['o', '1', 'x', 'x', 'o', 'o', '@', 'o', 'o', 'o'], ['o', 'o', 'x', '@', 'o', 'x', 'o', 'o', '@', 'x'], ['o', '@', 'o', 'o', 'o', 'x', 'x', '@', '2', 'x']])
        self.assertEqual(self.t5.gettabuleiro(), [['o', 'o', 'o', '@', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', '@', 'x', 'o', '1', 'x', '@', 'x', '@', 'o'], ['o', 'x', 'o', 'o', '@', 'o', 'o', 'o', '3', '@'], ['o', '@', 'o', 'o', '1', 'x', 'o', 'o', '@', 'o'], ['o', 'x', 'o', '0', 'x', 'x', 'x', 'o', '1', 'o'], ['o', 'x', '@', '1', 'x', 'x', 'x', '@', 'x', 'o'], ['@', 'o', 'o', 'o', 'x', '0', 'o', 'o', '@', 'o'], ['o', '1', 'o', 'o', '@', 'o', 'o', 'o', '2', 'o'], ['o', '@', '2', '@', '2', '2', '@', 'x', '@', 'o'], ['o', 'o', 'o', 'o', 'o', '@', 'o', 'o', 'o', 'o']])
        self.assertEqual(self.t6.gettabuleiro(), [['o', 'o', '@', 'x', 'o', 'o', '@'], ['o', 'o', 'o', '@', 'o', 'o', 'o'], ['@', 'o', 'o', '3', '@', 'o', 'o'], ['2', 'o', '1', '@', '2', 'o', '0'], ['@', 'o', 'o', '2', 'o', '@', 'o'], ['o', 'o', 'o', '@', 'o', 'o', 'o'], ['o', '@', 'o', '1', 'o', 'o', '@']])
        self.assertEqual(self.t7.gettabuleiro(), [['x', '@', '2', 'o', 'o', '@', 'o', 'o', 'x', '1', '@', 'x', '@', 'x'], ['@', 'x', '@', 'o', 'o', 'o', '1', '@', 'o', 'o', 'o', 'x', '3', '@'], ['x', 'x', 'o', '@', 'o', 'o', 'o', 'o', 'o', 'o', '0', 'o', '@', 'x'], ['o', '@', '1', 'o', 'o', 'o', '@', '1', 'o', '@', 'o', 'o', 'o', 'o'], ['x', 'o', 'o', 'o', '@', '2', '1', 'o', 'o', 'o', 'o', '@', 'o', 'o'], ['x', 'o', 'o', 'o', 'o', '@', 'o', '1', '@', '2', '@', 'o', 'o', 'o'], ['o', 'o', '@', '1', 'o', '2', '0', 'x', 'o', '0', 'o', 'o', 'x', 'o'], ['@', 'x', 'o', 'o', 'x', '@', 'x', 'x', 'x', 'o', 'x', 'o', 'o', '@'], ['o', 'o', 'o', '@', '2', 'o', 'x', 'o', 'o', 'o', '@', 'o', 'o', '1'], ['o', 'o', 'o', 'o', '@', 'o', 'o', '0', '0', 'o', 'o', 'o', '@', '2'], ['o', '@', 'o', 'o', 'o', 'o', '1', 'o', 'o', '@', 'o', '0', 'o', '@'], ['1', 'o', 'o', '0', 'o', 'o', '@', 'o', 'o', 'o', 'o', 'o', 'x', 'x'], ['@', 'x', 'x', 'o', 'o', 'o', 'o', '1', 'o', 'o', 'o', '@', 'x', '@'], ['x', '@', 'x', '@', 'x', 'x', 'o', '@', 'o', 'o', 'o', 'x', '@', 'x']])
        self.assertEqual(self.t8.gettabuleiro(), [['o', '@', 'o', '0', '2', '@', 'o'], ['o', 'o', 'o', 'o', '@', 'o', 'o'], ['x', 'o', 'o', 'o', 'o', 'o', '@'], ['0', 'o', 'o', '1', 'o', 'o', '1'], ['o', 'o', 'o', '@', 'o', 'o', 'x'], ['o', 'o', '@', 'o', 'o', 'o', 'o'], ['@', 'o', '1', 'x', 'o', 'o', '@']])
        self.assertEqual(self.t9.gettabuleiro(), [['o', 'o', 'o', 'o', '@', 'o', 'o', 'x', '@', 'o', '2', '@', 'o', 'o'], ['o', '1', '@', '1', 'o', 'o', 'o', 'o', 'o', 'o', '@', 'o', '1', 'o'], ['@', 'o', 'o', '0', 'o', '@', 'o', 'x', 'x', 'o', 'o', 'o', '@', 'o'], ['1', 'o', 'o', 'x', 'x', 'o', 'o', '@', '3', '@', 'x', 'x', '1', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '@', 'o', 'x', 'o', 'o', '@'], ['@', 'o', 'x', '1', 'o', 'x', 'o', 'x', 'x', 'o', 'o', 'o', '@', 'o'], ['x', 'o', 'x', '@', 'o', 'x', 'o', '@', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', '@', 'o', 'x', 'o', '@', 'x', 'o', '1'], ['o', 'o', 'o', 'o', '@', 'x', '2', 'o', '0', 'o', 'x', 'x', 'o', '@'], ['o', '@', 'o', '0', 'o', 'o', '@', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', '1', 'x', 'x', 'o', '0', 'o', 'o', '@', '2', '1', '@', 'o', '1'], ['@', 'o', 'o', 'o', 'o', '0', 'x', 'o', 'o', '@', 'x', 'o', 'o', '@'], ['o', '1', 'o', 'o', 'o', 'o', '@', 'o', 'o', 'o', 'x', 'o', '1', 'o'], ['o', '@', 'o', '0', 'o', '@', '2', 'o', 'o', 'o', 'o', 'o', '@', 'o']])
        self.assertEqual(self.t10.gettabuleiro(), [['o', 'o', '@', 'x', 'o', '1', '@', '2', '@', 'x', 'o', '@', '1', 'o', '@', 'o', '0', 'o', 'o', '@', 'o', '0', 'o', 'o', '@'], ['o', '0', 'x', 'o', '@', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '0', 'o', 'o', '1', 'x', '0', 'o'], ['@', 'x', 'o', '0', 'o', 'x', 'x', '0', 'x', 'x', 'o', 'o', 'o', 'x', 'x', 'x', 'x', 'o', 'o', 'o', 'o', '@', 'o', 'x', 'o'], ['1', '1', 'o', 'o', 'o', '@', 'o', 'x', 'o', '@', 'o', '0', 'o', '@', 'o', 'x', '@', 'o', '0', 'o', 'o', 'o', '1', 'o', 'x'], ['o', '@', 'o', 'o', 'o', 'o', 'o', '2', '@', 'x', '@', 'o', 'o', 'x', '@', 'o', 'x', 'x', 'o', 'o', 'o', 'o', '@', 'o', 'o'], ['o', 'o', 'o', '@', 'o', 'o', 'x', '@', 'o', 'o', 'x', 'x', 'o', '@', 'x', '0', 'o', 'x', '@', 'o', 'o', 'o', 'x', 'o', 'x'], ['o', 'x', '@', '2', 'o', 'o', 'x', 'o', 'o', 'x', '@', 'o', 'o', 'o', 'x', 'o', '@', 'x', 'x', '1', '@', 'o', 'x', 'o', '@'], ['@', 'o', 'o', 'o', '0', '0', '1', 'x', 'o', 'x', '1', 'o', '@', '1', 'x', '@', 'o', '1', '@', 'o', '1', 'x', 'x', 'o', 'x'], ['2', 'o', '1', '@', 'x', 'o', '@', 'o', '1', '@', 'o', 'o', 'o', 'o', 'x', 'x', '1', 'o', 'o', 'o', 'o', '@', '1', 'o', '@'], ['@', 'o', 'x', 'x', 'o', '0', 'o', '@', 'x', 'x', '1', '@', 'o', 'o', 'x', 'x', '@', 'x', '2', '@', 'x', 'o', '1', 'o', '1'], ['o', 'o', '0', 'o', '@', 'x', 'x', 'x', 'x', 'x', 'x', 'o', 'o', 'x', 'x', '0', 'o', '2', '@', 'x', 'o', 'o', '@', 'o', 'o'], ['o', '@', 'x', '@', 'x', '@', 'o', '0', 'o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', '@', 'o', 'x', '@', 'x', 'o', '@', 'o'], ['1', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '@', 'o', 'o', 'o', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '@', 'o', 'o', '0'], ['@', 'o', 'o', 'x', 'o', 'x', 'o', 'o', 'o', '@', 'o', 'o', 'o', 'o', '1', '@', 'o', 'x', 'o', '@', 'x', 'o', '0', 'o', 'o'], ['o', 'o', 'o', 'o', '@', '2', '@', '1', 'o', '1', 'x', '0', 'o', 'o', 'x', 'x', 'x', 'x', 'x', 'x', 'o', 'o', '0', 'o', '@'], ['x', 'o', '1', '@', 'x', 'o', 'x', 'x', 'o', 'x', 'x', 'o', '@', 'o', '0', 'x', '1', '@', 'o', '1', '@', '1', 'x', 'o', 'o'], ['@', 'o', '0', 'o', 'o', 'o', 'o', '@', '2', 'x', '0', 'o', 'o', '@', 'o', 'o', 'x', 'o', '@', 'o', 'x', 'o', 'x', 'o', '0'], ['2', 'o', 'x', 'x', 'x', '@', 'o', '2', '@', 'o', 'x', 'x', 'o', 'o', 'x', '0', 'o', '1', 'x', 'x', 'x', '@', 'o', 'o', 'o'], ['@', 'o', '0', 'o', 'o', 'x', '0', 'x', 'o', '@', 'x', 'o', 'o', 'o', '@', 'x', 'o', '@', '1', 'o', 'o', '2', 'o', 'x', '@'], ['x', 'o', '0', 'o', '@', 'o', 'o', 'x', 'o', 'x', 'x', '@', 'o', 'x', '1', 'o', '@', 'o', '1', 'o', 'o', '@', 'o', 'o', 'o'], ['@', 'o', 'o', 'o', 'o', 'o', 'o', 'x', 'x', '@', 'o', '1', 'o', '@', 'o', 'x', 'o', 'x', '@', 'o', 'o', 'o', 'o', 'o', 'o'], ['1', 'o', 'x', '@', 'o', 'o', '0', 'o', '@', 'x', '@', 'o', 'o', 'x', 'o', '@', 'o', '0', 'o', '@', 'o', 'o', 'o', 'x', 'x'], ['o', '1', '@', 'o', 'o', 'o', 'o', 'o', '1', 'x', 'x', '0', 'o', 'o', '@', '2', 'x', 'x', '1', 'x', 'o', 'x', '@', '1', 'o'], ['o', '0', 'x', '0', 'o', 'o', '0', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '@', 'o', 'o', 'o', 'x', '0', 'o'], ['@', 'o', 'o', '0', 'o', '@', 'o', 'o', '0', 'o', '@', 'o', '1', '@', 'o', 'x', '@', 'x', 'o', '1', '@', '1', 'o', 'o', '@']])


    def verify_lights(self, tab):
        for lin in range(len(tab)):
            for col in range(len(tab[lin])):
                if tab[lin][col] in "-.":
                    return False
        return True
    
if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit = False)