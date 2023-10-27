# will be called from execution to generate questions
from utils.local_queries import get_random_country, get_country_capital


class Question:

    # will contain the templates to our questions
    # calls dbpedia_utils and local_queries scripts (+additional) to fill templates with data
    #     --> might be even useful to have a separate script which puts the data for the questions together (data with
    #         correct and wrong answers)
    def __init__(self, dataHandler):
        self.localData = dataHandler

    def questionCapitalOfCountry(self):
        #has to return a dictionary with the (1) filled template, (2) correct answer and (3) false answers
        template = "What is the capital of {country}"

        country, capital_uri = get_random_country(self.localData.rdf_countries)
        capital = get_country_capital(capital_uri, self.localData.rdf_capitals)

        question = {"template": template.format(country=country),
                    "return": "The capital of {country} is {capital}".format(country=country, capital=capital),
                    "correct answer": capital,
                    "wrong answers": ["0", "1", "2"]}
        return question