"""Module allow to get the coordinate of a spécifique city."""

from app.config import URL, api_key
from app.parser import Parser
from app.wikipedia import Wikipedia


import requests


class GoogleMap:
    """Class manage the call to the googleMap API."""

    def get_coordinate(self, city):
        """[summary].

        :param city: place you want to find the coordinate
        :type city: [str]
        :return: [A dictionnary with the latitude et longitude]
        :rtype: [List]
        """
        try:
            config = {
                "address": city,
                "key": api_key,
            }
            res = requests.get(URL, params=config)
            if res.status_code == 200:
                results = res.json()
                adresse = results["results"][0]["formatted_address"]
                lat = results["results"][0]["geometry"]["location"]["lat"]
                lng = results["results"][0]["geometry"]["location"]["lng"]
        except requests.exceptions.HTTPError as err:
            print("Http error:", err)
        # Manage if there is a connection error
        except requests.exceptions.ConnectionError as errc:
            print("You have a connection error: ", errc)
        return {"latitude": lat, "longitude": lng, "adresse": adresse}


if __name__ == "__main__":
    a = Parser("Paris")
    b = a.process()
    c = GoogleMap()
    d = Wikipedia()
    e = d.get_article_id(
        c.get_coordinate(b)["latitude"], c.get_coordinate(b)["longitude"]
    )
    f = d.get_article(e)

