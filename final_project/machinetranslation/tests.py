import unittest
from translator import english_to_french, french_to_english
class TestEnglishToFrech(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('bread'), 'pain') 
        self.assertEqual(english_to_french('lion'), 'lion') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNone(english_to_french(),"Null input")

    
class Testfrench_to_english(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('pomme'), 'apple') 
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye') 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertIsNone(french_to_english(),"Null input")



unittest.main()
