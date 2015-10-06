import unittest
from language_detector import LanguageDetector


class LanguageDetectorTests(unittest.TestCase):

    def setUp(self):
        self.detector = LanguageDetector()

    def test_language_not_detected(self):
        self.assertEqual('Language not detected', self.detector.guess_language(''))

    def test_dutch_detected(self):
        message = "de het en een"
        self.assertEqual('Dutch', self.detector.guess_language(message))

    def test_english_detected(self):
        message = "the it and a"
        self.assertEqual('English', self.detector.guess_language(message))

    def test_german_detected(self):
        message = "der die das und"
        self.assertEqual('German', self.detector.guess_language(message))

    def tearDown(self):
        print "Finished test {0}".format(self._testMethodName)