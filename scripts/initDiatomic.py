from py2neo import Graph
from py2neo import Node
from py2neo import Relationship

graph = Graph("bolt://neo4jdatabase-container:7687", auth=("neo4j", "test"))

results = graph.run(
    """CALL semantics.importRDF("file:///import/ontologies/diatomic.ttl",  "Turtle",{ languageFilter: "en" })"""
)

results = graph.run(
    """MATCH (a)-[b]-(c:Resource { uri: "https://diatomic.eglobalmark.com/ontology#Beekeeper"})  RETURN *"""
).data()
print(results[0])

