from py2neo import Graph
from py2neo import Node
from py2neo import Relationship

graph = Graph("bolt://neo4jdatabase-container:7687", auth=("neo4j", "test"))
alice = Node("Person", name="Alice")
pino = Node("Person", name="Pino")
tx = graph.begin()
tx.create(pino)
tx.create(alice)


banana = Node("Fruit", "Food", colour="yellow", tasty=True)
bob = Node.cast({"name": "Bob Robertson", "age": 44})
alice_knows_bob = Relationship(alice, "KNOWS", bob, since=1999)
tx.create(alice_knows_bob)
tx.commit()

print(alice_knows_bob)
results = graph.run("MATCH (n:Person) RETURN n.name").data()
print(results)