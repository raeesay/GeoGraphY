from rdflib import Graph
import random
# TODO: Exception handling

# What is the capital of {country}?
# -> We want to be able to query a country first for the question
# Then get the answer by using the geographis:capital tag

def get_random_country(rdf_countries):

    # Generate a random offset
    max_offset = 240  
    random_offset = random.randint(0, max_offset)

    # Query a random country
    query_country = f"""
        PREFIX gn: <http://www.geonames.org/ontology#>
        PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>
        PREFIX code: <http://telegraphis.net/data/countries/codeSchemes#>

        SELECT ?country ?name ?capital_uri
        WHERE {{
            ?country a gn:Country ;
                    gn:name ?name ;
                    geographis:capital ?capital_uri .
        }}
        LIMIT 1
        OFFSET {random_offset}
    """


    country_name = None
    capital_uri = None

    for row in rdf_countries.query(query_country):
        country_name = row[1]
        capital_uri = row[2]
        
    return country_name, capital_uri

def get_country_capital(capital_uri, rdf_capitals):

    # Query for the capital's name using the correct relationship
    query_capital = f"""
        PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>
        PREFIX gn: <http://www.geonames.org/ontology#>

        SELECT ?capital_name
        WHERE {{
            <{capital_uri}> gn:name ?capital_name .
        }}
    """

    capital_name = None

    for capital_row in rdf_capitals.query(query_capital):
        capital_name = capital_row[0]

    return capital_name