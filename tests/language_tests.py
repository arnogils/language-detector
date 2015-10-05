import unittest
from language import Language


class LanguageTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_needs_capital(self):
        self.assertRaises(ValueError, Language, 'dutch', 'language_files/nl.txt')

    def test_name_must_be_string(self):
        self.assertRaises(ValueError, Language, '12345', 'language_files/nl.txt')

    def test_invalid_language_file(self):
        self.assertRaises(IOError, Language, 'Dutch', '')

    def tearDown(self):
        pass