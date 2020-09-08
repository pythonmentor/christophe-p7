"""Module to manage the parsing of the input sentence."""
from app.google_map import GoogleMap
from app.parser import Parser

from flask import render_template, request, jsonify, make_response
from app import my_app


@my_app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@my_app.route("/process", methods=["POST"])
def process():
    req = request.get_json()
    parser = Parser(req["message"])
    run_parser = parser.process()
    google_map = GoogleMap()
    coordinate = google_map.get_coordinate(run_parser)
    return make_response(jsonify(coordinate))
