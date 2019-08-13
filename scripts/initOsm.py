from py2neo import Graph
from py2neo import Node
from py2neo import Relationship

graph = Graph("bolt://neo4jdatabase-container:7687", auth=("neo4j", "test"))

results = graph.run(
    """CALL semantics.importRDF("file:///import/ontologies/OSM_Semantic_Network-2012-09-03.skos.rdf","RDF/XML")"""
).data()

print("****************")
results = graph.run(
    "MATCH (n)-[r]->(m) RETURN n, r, m;"
).data()
print(results)

