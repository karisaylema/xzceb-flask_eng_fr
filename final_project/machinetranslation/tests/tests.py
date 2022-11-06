import unittest
from translator import english_to_french, french_to_english
class TestEnglishToFrech(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('bread'), 'Pain') 
    def test2(self):
        self.assertEqual(english_to_french('lion'), 'Lion') 
    def test3(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test4(self):
        self.assertIsNone(english_to_french(None),"")

    
class Testfrench_to_english(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('pomme'), 'Apple') 
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye') 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertIsNone(french_to_english(None),"")



unittest.main()
