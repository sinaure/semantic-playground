# Playground to interact with neo4j with python library 

#### setup container
```
make build run
```
#### run script to inject jsonld objects
```
make exec
```
#### import the ontology (out of scope)
```
docker exec -i neo4jscript-container sh -c "python  scripts/initDiatomic.py"
```
#### import an Openstreetmap rdf (out of scope + fail)
```
docker exec -i neo4jscript-container sh -c "python /scripts/importOsm.py"
```


find the needed jar here (then put them in plugin folder):

https://github.com/jbarrasa/neosemantics
https://github.com/neo4j-contrib/neo4j-apoc-procedures
https://github.com/neo4j-contrib/spatial


