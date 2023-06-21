import unittest

from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase): 
    def test_en_to_fr(self): 
        self.assertEqual(english_to_french("Hello"), "Pepitoooo")
        en_1 = 'Ukraine claims to have shot down 32 of 35 Shahad drones overnight.'
        fr_1 = "L'Ukraine affirme avoir abattu 32 des 35 drones Shahad dans la nuit."
        self.assertEqual(english_to_french(en_1), fr_1)

class test_french_to_english(unittest.TestCase): 
    def test_fr_to_en(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        fr_2 = 'les egouts sont les tuyaux sous la terre'
        en_2 = 'the sewers are the pipes under the ground'
        self.assertEqual(french_to_english(fr_2), en_2) 

unittest.main()
