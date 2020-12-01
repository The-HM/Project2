from Project2_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField


class MovieReviewSearch(FlaskForm):
    title = StringField("New York Times Title")
    order = RadioField("Order by:",
                           choices=[('br', 'By Rating'),
                                    ('bh', 'By Headline'),
                                    ('bpd', 'By Publication Date')])

    critics_picks = SelectField("Select a filter:",
                         choices=[('Y', 'Filter by Picks'),
                                  ('', 'No Filter')])


def movie_search(title, order, critics_picks):
    api_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Documents/api_keys.json")
    api_key = api_key_dict["my_ny_key"]

    url = "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=" + title + "&" + "critics-pick=" + critics_picks + "&" + "order=" + order + ";" + "&api-key=" + api_key

    response = requests.get(url).json()
    "https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=godfather&api-key=yourkey"
    main_functions.save_to_file(response, "Project2_Flask/JSON_Documents/response.json")

    response_dict = main_functions.read_from_file("Project2_Flask/JSON_Documents/response.json")
    print(url)
    return response_dict
