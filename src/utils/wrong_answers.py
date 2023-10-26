import random

def wrong_answers_country(rdf_countries, right_answer):
    """
    - Function to retrieve wrong answers for a question with countries as answers
    - Inputs
        - countries rdf file
        - right_answer to the corresponding question in form of a country URI
        - STILL MISSING: optional continent URI!!!
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

    wrong_answers = []

    for row in rdf_countries.query(query_country):
        wrong_answers.append(row.country_uri)

    return wrong_answers

def wrong_answers_capital(rdf_countries, right_answer):
    """
        - Function to retrieve wrong answers for a question with countries as answers
        - Inputs
            - countries rdf file
            - right_answer to the corresponding question in form of a captial URI
        - Returns a list of 3 captial URIs of 3 randomly chosen countries
        """

    # Query 3 random capitals
    query_capital = f"""
            PREFIX gn: <http://www.geonames.org/ontology#>
            PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>

            SELECT ?capital_uri
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