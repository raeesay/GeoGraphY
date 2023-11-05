# will be called from execution to generate questions
from utils.local_queries import *
from utils.dbpedia_utils import *
from utils.wrong_answers import *


class Question:

    # will contain the templates to our questions
    # calls dbpedia_utils and local_queries scripts (+additional) to fill templates with data
    #     --> might be even useful to have a separate script which puts the data for the questions together (data with
    #         correct and wrong answers)
    def __init__(self, dataHandler):
        self.localData = dataHandler

    def questionCapitalOfCountry(self):
        #returns dictionary with the (1) filled template, (2) return sentence, (3) correct answer and (4) false answers
        template = "What is the capital of {country}?"

        country, capital_uri = get_random_country(self.localData.rdf_countries)
        capital = get_country_capital(capital_uri, self.localData.rdf_capitals)
        wrong_answers_uri = wrong_answers_capital(self.localData.rdf_countries, capital_uri)
        wrong_answers = [get_country_capital(cap_uri, self.localData.rdf_capitals) for cap_uri in wrong_answers_uri]

        question = {"template": template.format(country=country),
                    "return": "The capital of {country} is {capital}".format(country=country, capital=capital),
                    "correct answer": capital,
                    "wrong answers": wrong_answers}
        return question

    def questionDiallingCodeOfCountry(self):
        template = "What is the dialling code of {country}?"

        local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
        code = dbp_countryCode(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        while (not dbp_empty_return(code)):
            print("retrying to get a country with an existing dialling code!")
            local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
            code = dbp_countryCode(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        wrong_answers = wrong_answers_countryCode(code)


        question = {"template": template.format(country=country),
                    "return": "The dialling code of {country} is {code}".format(country=country, code=code),
                    "correct answer": code,
                    "wrong answers": wrong_answers}
        return question


    def questionAirportCountryLocation(self):
        template = "Which country is the airport {airport} located in?"

        local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
        airport = dbp_cityServed(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        while (not dbp_empty_return(airport)):
            print("retrying to get a country with an airport!")
            local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
            airport = dbp_cityServed(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        wrong_answers_uri = wrong_answers_country(self.localData.rdf_countries, local_country_uri)
        wrong_answers = [get_country_name(country_uri, self.localData.rdf_countries) for country_uri in wrong_answers_uri]

        question = {"template": template.format(airport=airport),
                    "return": "The airport {airport} is located in {country}".format(country=country, airport=airport),
                    "correct answer": country,
                    "wrong answers": wrong_answers}

        return question


    def questionNationalAnthem(self):
        template = "In which country is {anthem} used as a national anthem?"

        local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
        anthem = dbp_nationalAnthem(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        while (not dbp_empty_return(anthem)):
            print("retrying to get a country with a national anthem!")
            local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
            anthem = dbp_nationalAnthem(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        wrong_answers_uri = wrong_answers_country(self.localData.rdf_countries, local_country_uri)
        wrong_answers = [get_country_name(country_uri, self.localData.rdf_countries) for country_uri in wrong_answers_uri]

        question = {"template": template.format(anthem=anthem),
                    "return": "The national anthem of {country} is {anthem}".format(country=country, anthem=anthem),
                    "correct answer": country,
                    "wrong answers": wrong_answers}

        return question

    def questionPersonBorn(self):
        template = "In which country was {person} born?"

        local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
        person = dbp_birthPlace(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        while (not dbp_empty_return(person)):
            print("retrying to get a person born in a country!")
            local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
            person = dbp_birthPlace(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        wrong_answers_uri = wrong_answers_country(self.localData.rdf_countries, local_country_uri)
        wrong_answers = [get_country_name(country_uri, self.localData.rdf_countries) for country_uri in wrong_answers_uri]

        question = {"template": template.format(person=person),
                    "return": "{person} was born in {country}".format(country=country, person=person),
                    "correct answer": country,
                    "wrong answers": wrong_answers}

        return question

    def questionLeaderName(self):
        template = "Which country is lead by {person}?"

        local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
        person = dbp_leaderName(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        while (not dbp_empty_return(person)):
            print("retrying to get the leaders of a country!")
            local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
            person = dbp_leaderName(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        wrong_answers_uri = wrong_answers_country(self.localData.rdf_countries, local_country_uri)
        wrong_answers = [get_country_name(country_uri, self.localData.rdf_countries) for country_uri in wrong_answers_uri]

        question = {"template": template.format(person=person),
                    "return": "{country} is lead by {person}".format(country=country, person=person),
                    "correct answer": country,
                    "wrong answers": wrong_answers}

        return question

    def questionLeaderNameEasy(self):
        template = "Which country is lead by {person}?"

        local_country_uri, country = get_random_country_uri_easy(self.localData.rdf_countries)
        person = dbp_leaderName(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        while (not dbp_empty_return(person)):
            print("retrying to get the leaders of a country!")
            local_country_uri, country = get_random_country_uri_easy(self.localData.rdf_countries)
            person = dbp_leaderName(get_dbp_uri(self.localData.rdf_countries, local_country_uri))

        wrong_answers_uri = wrong_answers_country(self.localData.rdf_countries, local_country_uri)
        wrong_answers = [get_country_name(country_uri, self.localData.rdf_countries) for country_uri in wrong_answers_uri]

        question = {"template": template.format(person=person),
                    "return": "{country} is lead by {person}".format(country=country, person=person),
                    "correct answer": country,
                    "wrong answers": wrong_answers}

        return question

    def questionCurrencyInCountry(self):
        #returns dictionary with the (1) filled template, (2) return sentence, (3) correct answer and (4) false answers
        template = "What is the currency in {country}?"

        local_country_uri, country = get_random_country_uri(self.localData.rdf_countries)
        currency_uri = get_currency_uri(self.localData.rdf_countries, local_country_uri)
        #currency = get_currency_name(self.localData.rdf_currencies, currency_uri)
        wrong_answers_uri = wrong_answers_currency(self.localData.rdf_countries, currency_uri)
        #wrong_answers = [get_currency_name( self.localData.rdf_currencies, curr_uri) for curr_uri in wrong_answers_uri]

        question = {"template": template.format(country=country),
                    "return": "The currency in {country} is {currency}".format(country=country, currency=currency_uri),
                    "correct answer": currency_uri,
                    "wrong answers": wrong_answers_uri}
        return question