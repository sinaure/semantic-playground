from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

 
db = GraphDatabase("http://neo4jdatabase-container:7474",username="neo4j",password="test")
 

i="""CREATE INDEX ON :Resource(uri)"""
db.query(i)

q=("""MATCH (n)  DETACH DELETE n""")
results = db.query(q)
print(results[0])

#### this fail because http://spatial.ucd.ie/lod/osn/term/k:source/v:tiger_import Not found
i="""CALL semantics.importRDF("file:///import/ontologies/OSM_Semantic_Network-2012-09-03.skos.rdf","RDF/XML")"""
db.query(i)
q=("""MATCH (n) RETURN *""")
results = db.query(q)
print(results[0])
print("****************")
q=("""MATCH (n)-[r]->(m) RETURN n, r, m;""")
results = db.query(q)
print(results[0])

