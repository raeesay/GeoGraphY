from SPARQLWrapper import SPARQLWrapper, JSON

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

def dbp_json_to_list(json):
    """
    dbp_json_to_list
    - Function to retrieve the values from the dbpedia json
    - Only tested on a single 'column' being returned
    - The json must be provided
    - Returns a list
    """
    output = list()
    for object in json['results']['bindings']:
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

