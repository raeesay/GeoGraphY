from rdflib import Graph
from utils.local_queries import get_random_country, get_country_capital

# Load the RDF files
rdf_countries = Graph()
rdf_countries.parse("./src/data/countries.rdf", format="xml")

rdf_capitals = Graph()
rdf_capitals.parse("./src/data/capitals.rdf", format="xml")

if __name__ == "__main__":
    country, capital_uri = get_random_country(rdf_countries)
    capital = get_country_capital(capital_uri, rdf_capitals)

    print("Welcome to GeoGraphY!")
    print(f"What is the capital of {country}")
    print(f"1. {capital}")
    
    x = input("Please choose the correct option: ")
    if x == "1":
        print(f"Correct! The capital of {country} is {capital}!")
    else:
        print(f"Sorry, the capital of {country} is {capital}.")

