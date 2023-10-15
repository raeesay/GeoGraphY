from SPARQLWrapper import SPARQLWrapper, JSON

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

def dbp_extract_o(s,p):
    """
    dbp_extract_o
    - Function to retrieve the select query
    - Assumes that the object is the target
    - The subject and predicate must be provided
    - The subject could be as it would be on dbpedia eg. dbr:Germany, or it can be the original URI
    - Returns a dictionary
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = dbp_select_o(s=s, p=p)
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
        if ((uri==True) & (object['object']['type']=='uri')):
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

# Question specific functions --------------------------------------------------------------------

def dbp_countryCode(country_uri):
    """
    dbp_countryCode
    - Function to retrieve the dialling code for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the dialling code
    """
    working = dbp_extract_o(s=country_uri, p="dbo:countryCode")
    return(dbp_json_to_list(working)[0])

def dbp_leaderName(country_uri):
    """
    dbp_leaderName
    - Function to retrieve the leaders' names for the country provided as input
    - The input can either be the URI or also dbp:Country
    - Returns a string with the leader names, with / between where there are multiple
    """
    working = dbp_extract_o(s=country_uri, p="dbp:leaderName")
    working = dbp_json_to_list(working)
    working = dbp_list_uri_to_text(working)
    return("/".join(working))

