# This file has the API URL's.

from API_Calls import *

api_url = "https://api.wheretheiss.at/v1/satellites/"


def before_scenario(context, scenario):
    context.api = API(api_url)


def after_scenario(context, scenario):
    pass
