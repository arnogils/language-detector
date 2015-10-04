"""Simple implementation of a language detector"""

import os
from io import open
from language import Language


class LanguageDetector:

    def __init__(self):
        self._languages = [Language('English', 'language_files/en.txt'),
                           Language('Dutch', 'language_files/nl.txt'),
                           Language('German', 'language_files/de.txt')]

    def guess_language(self, message):
        """Rough implementation of a language guessing algorithm.

        Args:
            Message: a message in string format.

        Returns:
            A string containing the name of the detected language.
        """
        matches = {}
        for language in self._languages:
            result = set(message.lower().split()) & language.keywords
            if result:
                matches[language.name] = result
        if not matches:
            return 'Language not detected'
        return max(matches, key=lambda k: len(matches[k]))

    def guess_from_files(self, directory):
        """Read messages from a directory and guess their language
        using the guess_language method.

        Args:
            Directory: the directory containing the messages.

        Prints:
            The detected language for each file in the directory.
        """
        for message in os.listdir(directory):
            with open(message, mode='rt', encoding='utf-8') as f:
                print self.guess_language(message)

    def guess_from_string(self, message):
        result = self.guess_language(message)
        print result