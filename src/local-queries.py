from rdflib import Graph
# TODO: Exception handling

# Load the RDF files
rdf_countries = Graph()
rdf_countries.parse("./src/data/countries.rdf", format="xml")

rdf_capitals = Graph()
rdf_capitals.parse("./src/data/capitals.rdf", format="xml")

# What is the capital of {country}?
# -> We want to be able to query a country first for the question
# Then get the answer by using the geographis:capital tag

# Query a random country
# TODO: Randomise the offset, this keeps returning "Senegal"
query_country = """
    PREFIX gn: <http://www.geonames.org/ontology#>
    PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>
    PREFIX code: <http://telegraphis.net/data/countries/codeSchemes#>

    SELECT ?country ?name ?capital_uri
    WHERE {
        ?country a gn:Country ;
                gn:name ?name ;
                geographis:capital ?capital_uri .
    }
    OFFSET 200
    LIMIT 1
"""

country_uri = None
country_name = None
capital_uri = None

for row in rdf_countries.query(query_country):
    country_uri = row[0]
    country_name = row[1]
    capital_uri = row[2]
    

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

print(f"The capital of {country_name} is {capital_name}")