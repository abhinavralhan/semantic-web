from rdflib import Graph, URIRef
graph = Graph()

graph.parse("http://dbpedia.org/data/Berlin.rdf", format = "xml")

for data in graph:
    print(f"{data}\n#############################")
    
def relatedTo(URI):
    predicate = URIRef(URI)
    for resources in graph.subjects(predicate):
        print(f"URI: {URI}, Resources: {resources}")

relatedTo("http://dbpedia.org/property/namedAfter")
relatedTo("http://dbpedia.org/property/registrationPlate")
relatedTo("http://dbpedia.org/property/image")
relatedTo("http://dbpedia.org/property/deathPlace")