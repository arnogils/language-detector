"""Simple implementation of a language detector"""

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

    def guess_from_string(self):
        raise NotImplementedError

    def guess_from_files(self):
        raise NotImplementedError

if __name__ == "__main__":
    x = LanguageDetector()
    print(x.guess_language('the'))