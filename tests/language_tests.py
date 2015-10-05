import unittest
from language import Language


class LanguageTests(unittest.TestCase):

    def setUp(self):
        self.language = Language('Dutch', '../language_files/nl.txt')

    def test_needs_capital(self):
        self.assertRaises(ValueError, Language, 'dutch', '../language_files/nl.txt')

    def test_name_must_be_string(self):
        self.assertRaises(AttributeError, Language, 10, '../language_files/nl.txt')

    def test_name_must_alpha(self):
        self.assertRaises(ValueError, Language, '1234', 'language_files/nl.txt')

    def test_invalid_language_file(self):
        self.assertRaises(IOError, Language, 'Dutch', '')

    def test_valid_name(self):
        self.assertEqual('Dutch', self.language.name)

    def test_file_to_set(self):
        self.assertIsInstance(self.language.keywords, set)

    def test_keyword_conversion_not_empty(self):
        self.assertGreater(len(self.language.keywords), 0)

    def tearDown(self):
        print "Finished test {0}".format(self._testMethodName)