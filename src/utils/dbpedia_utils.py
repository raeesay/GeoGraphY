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