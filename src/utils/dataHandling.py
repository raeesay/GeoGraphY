from rdflib import Graph

class DataHandler:

    # load local data into python
    # maybe even check for internet connection for dbpedia data --> throw exception/ if not available

    def __init__(self):
        # Load the RDF files
        self.rdf_capitals = self.getLocalData("capitals")
        self.rdf_continents = self.getLocalData("continents")
        self.rdf_countries = self.getLocalData("countries")
        self.rdf_currencies = self.getLocalData("currencies")
        self.checkInternetConnection()


    def getLocalData(self, name):
        graphObj = Graph()
        graphObj.parse("./src/data/{name}.rdf".format(name=name), format = "xml")
        return graphObj

    def checkInternetConnection(self):
        # optional for dbpedia data
        return