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

def get_dbp_uri(rdf_countries, country_uri):
    """
    - Function to retrieve the dbpedia URI of a country from local geography data
    - Input is the country URI from the local data and the countries rdf file
    """

    query_uri = f"""
                PREFIX gn: <http://www.geonames.org/ontology#>
                PREFIX owl: <http://www.w3.org/2002/07/owl#>

                SELECT ?dbp_uri
                WHERE {{
                    <{country_uri}> owl:sameAs ?dbp_uri
                    FILTER regex(str(?dbp_uri), "dbpedia")
                }}

            """
    dbp_uri = None

    for row in rdf_countries.query(query_uri):
        dbp_uri = row.dbp_uri

    return str("<"+str(dbp_uri)+">")

def get_random_country_uri(rdf_countries):
    """
    - Function to retrieve the URI of a randomly chosen country from local geography data
    - Input is the countries rdf file
    """
    # Generate a random offset
    max_offset = 240
    random_offset = random.randint(0, max_offset)

    # Query a random country
    query_country = f"""
            PREFIX gn: <http://www.geonames.org/ontology#>

            SELECT ?country_uri ?name
            WHERE {{
                ?country_uri a gn:Country.
                ?country_uri gn:name ?name.
            }}

            LIMIT 1
            OFFSET {random_offset}
        """

    country_uri = None
    country_name = None

    for row in rdf_countries.query(query_country):
        country_uri = row.country_uri
        country_name = row.name

    return country_uri, country_name


def get_random_country_uri_easy(rdf_countries):
    """
    - Function to retrieve the URI of a randomly chosen country from local geography data,
    where the population is above 30 million
    - Input is the countries rdf file
    """
    # Generate a random offset
    max_offset = 50
    random_offset = random.randint(0, max_offset)

    # Query a random country
    query_country = f"""
                PREFIX gn: <http://www.geonames.org/ontology#>

                SELECT ?country_uri ?name
                WHERE {{
                    ?country_uri a gn:Country.
                    ?country_uri gn:name ?name.
                    ?country_uri gn:population ?pop.
                    FILTER(xsd:integer(?pop)>30000000)
                }}

                LIMIT 1
                OFFSET {random_offset}
            """

    country_uri = None
    country_name = None

    for row in rdf_countries.query(query_country):
        country_uri = row.country_uri
        country_name = row.name

    return country_uri, country_name

def get_continent_uri(rdf_countries, country_uri):
    """
    - Function to retrieve the continent URI of a country
    - Input is a (local) country URI and the countries rdf file
    """
    query_continent = f"""
            PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>

            SELECT ?continent_uri
            WHERE {{
                <{country_uri}> geographis:onContinent ?continent_uri .
            }}
        """

    continent_uri = None

    for row in rdf_countries.query(query_continent):
        continent_uri = row.continent_uri

    return continent_uri

def get_currency_uri(rdf_countries, country_uri):
    """
    - Function to retrieve the currency URI of a country
    - Input is a (local) country URI and the countries rdf file
    """
    query_currency = f"""
            PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>

            SELECT ?currency_uri
            WHERE {{
                <{country_uri}> geographis:currency ?currency_uri .
            }}
        """

    currency_uri = None

    for row in rdf_countries.query(query_currency):
        currency_uri = row.currency_uri

    return currency_uri


def get_country_name(country_uri, rdf_countries):

        # Query for the country's name using the country uri
        query_country = f"""
            PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>
            PREFIX gn: <http://www.geonames.org/ontology#>

            SELECT ?country_name
            WHERE {{
                <{country_uri}> gn:name ?country_name .
            }}
        """

        country_name = None

        for country_row in rdf_countries.query(query_country):
            country_name = country_row[0]

        return country_name


def get_currency_name(rdf_currencies, currency_uri):
    # Query for the currency's name using the currency uri
    query_name = f"""
            PREFIX money: <http://telegraphis.net/ontology/money/money#>

            SELECT ?currency_name
            WHERE {{
                <{currency_uri}> money:name ?currency_name .
            }}
        """

    currency_name = None

    for name_row in rdf_currencies.query(query_name):
        currency_name = name_row.currency_name

    return currency_name

    for name_row in rdf_currencies.query(query_name, initBindings={'currency_uri': currency_uri}):
        currency_name = name_row.currency_name

    return currency_name