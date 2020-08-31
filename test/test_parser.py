"""module testing the parsing class."""

import unittest


from app.parser import Parser


class TestParsing(unittest.TestCase):
    """[summary].

    :param unittest: [description]
    :type unittest: [type]
    """

    def test_remove_accent(self):
        """[summary]."""
        accent = Parser("aéèàôrty")
        assert accent.remove_accent() == "aeeaorty"

    def test_remove_stop_words(self):
        """[summary]."""
        a = Parser("Salut Grandpy connais tu les vans ?")
        assert a.remove_stop_words("vans")

    def test_only_stop_word(self):
        """[summary]."""
        a = Parser("absolument afin ailleurs papybot")
        b = a.process()
        assert len(b) == 0

    def test_empty_sentence(self):
        """[summary]."""
        a = Parser("")
        b = a.process()
        assert len(b) == 0


if __name__ == "__main__":
    unittest.main()
