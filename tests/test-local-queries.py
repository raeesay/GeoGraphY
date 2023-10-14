from rdflib import Graph

# Print out each predicate in turtle format to give an overview
# Example from RDFLib documentation
def turtle_format(g):
    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")

    # Print the number of "triples" in the Graph
    print(f"Graph g has {len(g)} statements.")
    # Prints: Graph g has 86 statements.

    # Print out the entire Graph in the RDF Turtle format
    print(g.serialize(format="turtle"))

# Print all country names
def contents(g):
    # Query the data in g using SPARQL
    q = """
        PREFIX gn: <http://www.geonames.org/ontology#>
        PREFIX geographis: <http://telegraphis.net/ontology/geography/geography#>

        SELECT ?name
        WHERE {
            ?country a gn:Country ;
                    gn:name ?name .
        }
    """

    # Apply the query to the graph and iterate through results
    # With this query we print the country names
    for row in g.query(q):
        print(row["name"])

# Load the RDF files
rdf_countries = Graph()
rdf_countries.parse("./src/data/countries.rdf", format="xml")

rdf_capitals = Graph()
rdf_capitals.parse("./src/data/capitals.rdf", format="xml")

rdf_continents = Graph()
rdf_continents.parse("./src/data/continents.rdf", format="xml")

rdf_currencies = Graph()
rdf_currencies.parse("./src/data/currencies.rdf", format="xml")

turtle_format(rdf_countries)
contents(rdf_countries)