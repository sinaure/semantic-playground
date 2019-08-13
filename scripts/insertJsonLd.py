from py2neo import Graph
from py2neo import Node
from py2neo import Relationship
import sys

graph = Graph("bolt://neo4jdatabase-container:7687", auth=("neo4j", "test"))



graph.run("""CALL semantics.importRDF({file},'JSON-LD',{ handleVocabUris: 'SHORTEN', typesToLabels: true, commitSize: 500})""",
               file=sys.argv[1])


results = graph.run(
    "MATCH (n) RETURN *"
).data()
print(results)