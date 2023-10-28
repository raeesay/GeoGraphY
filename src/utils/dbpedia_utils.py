from SPARQLWrapper import SPARQLWrapper, JSON
import random
import re

# For sending requests to dbpedia ------------------------------------------------------------------

def dbp_select_o(s,p):
    """
    - Function to form the select query
    - Assumes that the object is the target
    - The subject and predicate must be provided
    - The subject could be as it would be on dbpedia eg. dbr:Germany, or it can be the original URI
    - Returns a string
    """
    query = "SELECT ?object WHERE {" + s + " " + p + " ?object.}"
    return(query)

def dbp_select_s(o,p):
    """
    - Function to form the select query
    - Assumes that the subject is the target
    - The object and predicate must be provided
    - The object could be as it would be on dbpedia eg. dbr:Germany, or it can be the original URI
    - Returns a string
    """
    query = "SELECT ?object WHERE {?object " + p + " " + o + ".}"
    return(query)

def dbp_extract(query):
    """
    dbp_extract
    - Function to retrieve the select query
    - The query must be provided
    - The subject could be as it would be on dbpedia eg. dbr:Germany, or it can be the original URI
    - Returns a dictionary
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return(results)

# For handling the returned data from dbpedia -----------------------------------------------------

def dbp_json_to_list(json, uri=True):
    """
    dbp_json_to_list
    - Function to retrieve the values from the dbpedia json
    - Only tested on a single 'column' being returned
    - The json must be provided
    - If uri=True, will only return items from the list that are uris
    - Returns a list
    """
    output = list()
    for object in json['results']['bindings']:
        if ((uri==True) & (object['object']['type']=='uri'))|(uri==False):
            output.append(object['object']['value'])
    return(output)

def dbp_uri_to_text(string):
    """
    dbp_uri_to_text
    - Function to retrieve the actual words from a dbpedia URI
    - The string containing the URI must be provided
    - Returns a string
    """
    return(string.rsplit('/', 1)[1].replace('_',' '))

def dbp_list_uri_to_text(string_list):
    """
    dbp_list_uri_to_text
    - Function to retrieve the actual words from a list of dbpedia URI
    - The list containing strings with URIs must be provided
    - Returns a list of strings
    """
    return([dbp_uri_to_text(string) for string in string_list])

def dbp_empty_return(fn_output):
    """
        dbp_empty_return
        - Function to check if the return from dbpedia is empty
        - Returns 1 if non-empty, 0 if empty
        """
    if fn_output=='':
        return(0)
    else:
        return(1)

# Question specific functions --------------------------------------------------------------------

def dbp_countryCode(country_uri):
    """
    dbp_countryCode
    - Function to retrieve the dialling code for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the dialling code
    """
    try:
        working = dbp_extract(dbp_select_o(s=country_uri, p="dbo:countryCode"))
        return(dbp_json_to_list(working, uri=False)[0])
    except:
        return('')

def dbp_leaderName(country_uri):
    """
    dbp_leaderName
    - Function to retrieve the leaders' names for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the leader names, with / between where there are multiple
    """
    try:
        working = dbp_extract(dbp_select_o(s=country_uri, p="dbp:leaderName"))
        working = dbp_json_to_list(working)
        working = dbp_list_uri_to_text(working)
        return("/".join(working))
    except:
        return('')

def dbp_birthPlace(country_uri):
    """
    dbp_birthPlace
    - Function to retrieve a person born in the country for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the name
    """
    try:
        working = dbp_extract(dbp_select_s(o=country_uri, p="dbo:birthPlace"))
        working = dbp_json_to_list(working)
        working = random.choice(working)
        working = dbp_uri_to_text(working)
        return(working)
    except:
        return('')

def dbp_cityServed(country_uri):
    """
    dbp_cityServed
    - Function to retrieve a random airport for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the name
    - SAME AS birthPlace
    """
    try:
        working = dbp_extract(dbp_select_s(o=country_uri, p="dbp:cityServed"))
        working = dbp_json_to_list(working)
        working = random.choice(working)
        working = dbp_uri_to_text(working)
        return(working)
    except:
        return('')

def dbp_nationalAnthem(country_uri):
    """
    dbp_nationalAnthem
    - Function to retrieve the national anthem for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the national anthem, unnecessary quote marks also removed
    """
    try:
        working = dbp_extract(dbp_select_o(s=country_uri, p="dbp:nationalAnthem"))
        working = dbp_json_to_list(working, uri=False)
        return(working[0].replace('"',""))
    except:
        return('')

def dbp_mouthLocation(country_uri):
    """
    dbp_mouthLocation
    - Function to retrieve a river with the mouth in the country for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with a river name, additional info in brackets removed
    """
    try:
        working = dbp_extract(dbp_select_s(o=country_uri, p="dbp:mouthLocation"))
        working = dbp_json_to_list(working)
        working = random.choice(working)
        working = dbp_uri_to_text(working)
        return(re.sub(" \(.*?\)","",working))
    except:
        return('')

def dbp_locationCountry(country_uri):
    """
    dbp_locationCountry
    - Function to retrieve an architectural structure for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with a building name, additional info in brackets removed
    - If not narrowed to Architectural Structure, was too challenging
    """
    try:
        query = "SELECT ?object WHERE {?object dbp:locationCountry " + country_uri + ". ?object rdf:type dbo:ArchitecturalStructure.}"
        working = dbp_extract(query)
        working = dbp_json_to_list(working)
        working = random.choice(working)
        working = dbp_uri_to_text(working)
        return(re.sub(" \(.*?\)","",working))
    except:
        return('')
