"""Module to manage the parsing of the input sentence."""
import re
import unicodedata

from app.config import STOP_WORDS


class Parser:
    """Class allow to isolate keyword to send to the google map api."""

    def __init__(self, sentence):
        """Construct the parser instance.

        :param sentence: input from user
        :type sentence: [str]
        """
        self.sentence = sentence

    def remove_accent(self):
        """Remove all accent from the sentence.

        :return: [sentence without accent]
        :rtype: [str]
        """
        try:
            self.sentence = unicode(text, "utf-8")
        except NameError:  # unicode is a default on python 3
            pass
        self.sentence = (
            unicodedata.normalize("NFD", self.sentence)
            .encode("ascii", "ignore")
            .decode("utf-8")
        )
        return str(self.sentence)

    def remove_stop_words(self, sentence):
        """Keep only usefull keyword remove all th stop words.

        :param sentence: sentence to remove stop word
        :type sentence: [str]
        :return: [List with only keyword]
        :rtype: [lst]
        """
        self.sentence = re.sub(
            r"[.!,;?\"\'<>./?@#$%^&*_~]", " ", self.sentence
        ).split()
        return ",".join([i for i in self.sentence if i not in STOP_WORDS])

    def process(self):
        """Methode to run the parsing methode.

        :return: return a liste with only keyword
        :rtype: [List]
        """
        return self.remove_stop_words(self.remove_accent())
