"""Module testing the GoogleMap class."""
from app.google_map import GoogleMap
import requests


class TestGoogleMap:
    """Testing google map api call."""

    def test_get_coordinate(self, monkeypatch):
        """Testing get coordinate function.

        :param monkeypatch: [monkeypatching]
        :type monkeypatch: [Monkeypatch]
        :return: [dictionnary with lattitude and longitude plus adresse]
        :rtype: [dict]
        """
        result = {
            "latitude": 48.856614,
            "longitude": 2.3522219,
            "adresse": "Paris, France",
        }

        def mockreturn(self, city):
            return result

        city = "Paris"
        monkeypatch.setattr(GoogleMap, "get_coordinate", mockreturn)
        google_map = GoogleMap()
        coordinate = google_map.get_coordinate(city)

        assert coordinate["adresse"] == "Paris, France"
        assert coordinate["latitude"] == 48.856614
        assert coordinate["longitude"] == 2.3522219
