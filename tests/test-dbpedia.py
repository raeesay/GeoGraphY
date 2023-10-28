import src.utils.dbpedia_utils as dbpu
from rdflib import Graph
import numpy as np
import time

def all_countries():
    """
    all_countries
    - Function to retrieve a list of all the dbpedia URIs for the countries in the local graph
    """
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
    output = [str(i.dbp_uri) for i in rdf_countries.query(q)]
    return(output)

def dbp_test_o(p, countries):
    """
    dbp_test_o
    - Function to first retrieve a list of all the countries with a specific predicate referring to them as the subject
    - Then counts how many of the locally retrieved countries appear in the list
    - Returns an integer
    """
    dbp_return = dbpu.dbp_json_to_list(dbpu.dbp_extract("SELECT DISTINCT ?object WHERE {?object a dbo:Country . ?object " + p + " ?item .}"))
    working = [i for i in dbp_return if i in countries]
    return len(working)

def dbp_test_s(p, countries):
    """
    dbp_test_s
    - Function to first retrieve a list of all the countries with a specific predicate referring to them as the object
    - Then counts how many of the locally retrieved countries appear in the list
    - Returns an integer
    """
    dbp_return = dbpu.dbp_json_to_list(dbpu.dbp_extract("SELECT DISTINCT ?object WHERE {?object a dbo:Country . ?item " + p + " ?object .}"))
    working = [i for i in dbp_return if i in countries]
    return len(working)

def dbp_test_s2(countries):
    """
    dbp_test_s2
    - Specific variation for the more complicated locatedIn query
    """
    dbp_return = dbpu.dbp_json_to_list(dbpu.dbp_extract("SELECT DISTINCT ?object WHERE {?object a dbo:Country . ?item dbp:locationCountry ?object . ?item rdf:type dbo:ArchitecturalStructure .}"))
    working = [i for i in dbp_return if i in countries]
    return len(working)

def dbp_test_all():
    """
    dbp_test_all
    - Function to run all the test counts
    - Prints the dictionary
    """
    country_list = all_countries()
    tests = {}
    tests['ALL'] = len(country_list)
    tests['countryCode'] = dbp_test_o('dbo:countryCode', country_list)
    time.sleep(2)
    tests['leaderName'] = dbp_test_o("dbp:leaderName", country_list)
    time.sleep(2)
    tests['birthPlace'] = dbp_test_s("dbo:birthPlace", country_list)
    time.sleep(2)
    tests['cityServed'] = dbp_test_s("dbp:cityServed", country_list)
    time.sleep(2)
    tests['nationalAnthem'] = dbp_test_o("dbp:nationalAnthem", country_list)
    time.sleep(2)
    tests['mouthLocation'] = dbp_test_s("dbp:mouthLocation", country_list)
    time.sleep(2)
    tests['locatedIn'] = dbp_test_s2(country_list)
    print(tests)

dbp_test_all()

# {'ALL': 246,
#  'countryCode': 188,
#  'leaderName': 226,
#  'birthPlace': 228,
#  'cityServed': 172,
#  'nationalAnthem': 162,
#  'mouthLocation': 73,
#  'locatedIn': 148}