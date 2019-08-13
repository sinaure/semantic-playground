from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

 
db = GraphDatabase("http://neo4jdatabase-container:7474",username="neo4j",password="test")
 

i="""CREATE INDEX ON :Resource(uri)"""
db.query(i)
i="""CREATE (:NamespacePrefixDefinition {
  `http://www.example.com/ontology/1.0.0#`: 'ex',
  `http://www.w3.org/1999/02/22-rdf-syntax-ns#`: 'rdf'})"""
db.query(i)

q=("""MATCH (n)  DETACH DELETE n""")
results = db.query(q)
print(results[0])


i="""CALL semantics.importRDF("https://www.w3.org/ns/org.ttl",  "Turtle",{ languageFilter: "en" })"""
db.query(i)


print("****************")
q=("""MATCH (n)-[r]->(m) RETURN n, r, m;""")
results = db.query(q)
print(results[0])

