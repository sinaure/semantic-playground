from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

 
db = GraphDatabase("http://neo4jdatabase-container:7474",username="neo4j",password="test")
 
# Create some nodes with labels
user = db.labels.create("User")
u1 = db.nodes.create(name="Marco")
user.add(u1)
u2 = db.nodes.create(name="Daniela")
user.add(u2)
 
beer = db.labels.create("Beer")
b1 = db.nodes.create(name="Punk IPA")
b2 = db.nodes.create(name="Hoegaarden Rosee")
# You can associate a label with many nodes in one go
beer.add(b1, b2)
