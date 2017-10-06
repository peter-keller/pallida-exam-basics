import unittest
from unique_chars import *

class TestFile(unittest.TestCase):
    
    def test_not_repeatable_characters(self):
        self.assertTrue(unique_characters("slma"))

    def test_repeatable_characters(self):
        self.assertFalse(unique_characters("aaaaa"))

    def test_no_word_to_examine(self):
        self.assertTrue(unique_characters(""))

    
if __name__ == '__main__':
    unittest.main()