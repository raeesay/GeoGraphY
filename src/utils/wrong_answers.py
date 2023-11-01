import random
from utils.dbpedia_utils import *

def wrong_answers_country(rdf_countries, right_answer):
    """
    - Function to retrieve wrong answers for a question with countries as answers
    - Inputs
        - countries rdf file
        - right_answer to the corresponding question in form of a country URI
    - Returns a list of 3 country URIs
    """

    # Query 3 random countries
    query_country = f"""
        PREFIX gn: <http://www.geonames.org/ontology#>

        SELECT ?country_uri
        WHERE {{
            ?country_uri a gn:Country;
                        geographis:onContinent ?continent_uri
            FILTER(?country_uri != <{right_answer}>)
        }}
        ORDER BY RAND()
        LIMIT 3
    """

    try:
        wrong_answers = []

        for row in rdf_countries.query(query_country):
            wrong_answers.append(row.country_uri)

    except:
        wrong_answers = []

        for row in ["http://telegraphis.net/data/countries/DE#DE", "http://telegraphis.net/data/countries/NE#NE", "http://telegraphis.net/data/countries/CL#CL", "http://telegraphis.net/data/countries/LA#LA"]:
            wrong_answers.append(row)

        wrong_answers = wrong_answers[0:3]

    return wrong_answers

def wrong_answers_country_continent(rdf_countries, right_answer, continent_uri):
    """
    - Function to retrieve wrong answers for a question with countries as answers that depend on continent
    - Inputs
        - countries rdf file
        - right_answer to the corresponding question in form of a country URI
        - continent URI
    - Returns a list of 3 country URIs
    """

    # Query 3 random countries
    query_country = f"""
        PREFIX gn: <http://www.geonames.org/ontology#>

        SELECT ?country_uri
        WHERE {{
            ?country_uri a gn:Country;
                        geographis:onContinent ?continent_uri
            FILTER(?country_uri != <{right_answer}> && ?continent_uri = <{continent_uri}>)
        }}
        ORDER BY RAND()
        LIMIT 3
    """

    wrong_answers = []

    for row in rdf_countries.query(query_country):
        wrong_answers.append(row.country_uri)

    return wrong_answers

def wrong_answers_capital(rdf_countries, right_answer):
    """
    - Function to retrieve wrong answers for a question with capitals as answers
    - Inputs
        - countries rdf file
        - right_answer to the corresponding question in form of a capital URI
    - Returns a list of 3 different capital URIs of 3 randomly chosen countries
    """

    # Query 3 random capitals
    query_capital = f"""
            PREFIX gn: <http://www.geonames.org/ontology#>
            PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>

            SELECT DISTINCT ?capital_uri
            WHERE {{
                ?country_uri a gn:Country;
                            geographis:capital ?capital_uri .
                FILTER(?capital_uri != <{right_answer}>)
            }}
            ORDER BY RAND()
            LIMIT 3
        """

    wrong_answers = []

    for row in rdf_countries.query(query_capital):
        wrong_answers.append(row.capital_uri)

    return wrong_answers

def wrong_answers_currency(rdf_countries, right_answer):
    """
    - Function to retrieve wrong answers for a question with currency as answers
    - Inputs
        - countries rdf file
        - right_answer to the corresponding question in form of a currency URI
    - Returns a list of 3 different currency URIs of 3 randomly chosen countries
    """

    # Query 3 random (distinct) currencies
    query_currency = f"""
            PREFIX gn: <http://www.geonames.org/ontology#>
            PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>

            SELECT DISTINCT ?currency_uri
            WHERE {{
                ?country_uri a gn:Country;
                            geographis:currency ?currency_uri .
                FILTER(?currency_uri != <{right_answer}>)
            }}
            ORDER BY RAND()
            LIMIT 3
        """

    wrong_answers = []

    for row in rdf_countries.query(query_currency):
        wrong_answers.append(row.currency_uri)

    return wrong_answers


def wrong_answers_countryCode(right_answer):
    """
    - Function to retrieve wrong answers for a question with dialling code as answers
    - Inputs
        - right_answer to the corresponding question in form of a dialling code
    - Returns a list of 3 dialling codes as strings
    """

    query_countryCode = f"""
        SELECT DISTINCT ?object
        WHERE {{
            ?country dbo:countryCode ?object
            FILTER(?object != <{right_answer}>)
        }}
    """

    working = dbp_extract(query_countryCode)
    working = dbp_json_to_list(working, uri=False)
    wrong_answers = random.sample(working, k=3)

    return wrong_answers

