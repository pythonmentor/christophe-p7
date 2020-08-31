"""Module allow to get the pages of a spécifique location in wikipedia."""
from app.config import WIKI_API_URL

import requests


class Wikipedia:
    """Class manage the call to the mediaWiki API."""

    def get_article_id(self, lat, long):
        """Methode to get a list of article using the lattitude and longitude.

        :param lat: [lattitude]
        :type lat: [FLOAT]
        :param long: [Longitude]
        :type long: [FLOAT]
        :return: [description]
        :rtype: [type]
        """
        try:
            config = {
                "action": "query",
                "format": "json",
                "list": "geosearch",
                "gscoord": f"{lat}|{long}",
                "gsradius": 10000,
            }
            res = requests.get(WIKI_API_URL, params=config)
            print(res.url)
            results = res.json()
        # Manage if there is a HTTP error
        except requests.exceptions.HTTPError as err:
            print("Http error:", err)
        except requests.exceptions.ConnectionError as errc:
            print("You have a connection error: ", errc)
        return results

    def get_article(self, results):
        """Methode to get a spécifique article with page_id parameter.

        :param results: [use the get_article_id methode as argument]
        :type results: [dict]
        :return: [return json file]
        :rtype: [dict]
        """
        page_id = results["query"]["geosearch"][0]["pageid"]
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts|info",
            "inprop": "url",
            "exchars": 1200,
            "explaintext": 1,
            "pageids": page_id,
        }
        res = res = requests.get(WIKI_API_URL, params=params)
        print(res.url)
        return res.json()
