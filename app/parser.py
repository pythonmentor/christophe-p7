"""Module to manage the parsing of the input sentence."""
from app.config import STOP_WORDS


class Parser:
    """[summary]."""

    def __init__(self, sentence):
        """[summary].

        :param sentence: [description]
        :type sentence: [type]
        """
        self.sentence = sentence

    def remove_stop_words(self):
        return self.sentence.strip()


if __name__ == "__main__":
    a = Parser(
        "salut granpy pourrais tu m indiquer où se situe le musée d art et d histoire de fribourgs il te plait"
    )
    print(a.remove_stop_words())

