from SPARQLWrapper import SPARQLWrapper, JSON
import random
import re
import src.utils.dbpedia_utils as dbpu
import src.utils.local_queries as lq
from rdflib import Graph

def all_countries():
    rdf_countries = Graph()
    rdf_countries.parse("./src/data/countries.rdf", format="xml")
    q = """
            PREFIX gn: <http://www.geonames.org/ontology#>
            SELECT ?dbp_uri
            WHERE {
                ?country_uri a gn:Country.
                ?country_uri owl:sameAs ?dbp_uri
                FILTER regex(str(?dbp_uri), "dbpedia")
            }
        """
    output = [str("<"+i.dbp_uri+">") for i in rdf_countries.query(q)]
    return(output)

country_list = all_countries()
