"""Rough representation of a language model.
Properties are used to streamline the initialization process.
"""

from io import open


class Language(object):

    def __init__(self, language, keywords_file):
        self.name = language
        self.keywords = keywords_file

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, language):
        if not isinstance(language, str):
            raise ValueError('Language must be string')

        if not language.isalpha():
            raise ValueError('Invalid language name')

        if not language[0].isupper():
            raise ValueError('Language must start with a capital')

        self.__name = language

    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords_file):
        """Parses language specific keywords to a usable set"""
        with open(keywords_file, mode='rt', encoding='utf-8') as f:
            self.__keywords = set(f.read().split('\n'))