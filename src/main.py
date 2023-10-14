from rdflib import Graph
from utils.local_queries import country_capital  # Updated import

# TODO: Exception handling

# Load the RDF files
rdf_countries = Graph()
rdf_countries.parse("./src/data/countries.rdf", format="xml")

rdf_capitals = Graph()
rdf_capitals.parse("./src/data/capitals.rdf", format="xml")

if __name__ == "__main__":
    country_capital(rdf_countries, rdf_capitals)
