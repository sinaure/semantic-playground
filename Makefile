# DOCKER TASKS

build: ## Build the image
		docker image build -t neo4jscript .

build-nc: ## Build the image without caching
		docker image build --no-cache -t neo4jscript .

run: ## Run container
		docker container run -d --rm -i  --net=egm --name neo4jscript-container --mount type=bind,src=//c/Users/asinatra/Desktop/ECLIPSE_WORKSPACE/algorithms/scripts,dst=/scripts neo4jscript 
		docker container run -d  --rm  --net=egm --name neo4jdatabase-container --env NEO4J_AUTH=neo4j/test -p 7474:7474 -p 7687:7687 -v /c/Users/asinatra/Desktop/ECLIPSE_WORKSPACE/algorithms/import:/import -v /c/Users/asinatra/Desktop/ECLIPSE_WORKSPACE/algorithms/data:/data  -v /c/Users/asinatra/Desktop/ECLIPSE_WORKSPACE/algorithms/plugins:/plugins -v /c/Users/asinatra/Desktop/ECLIPSE_WORKSPACE/algorithms/conf:/conf  neo4j:3.5
		docker container run -d --rm --net=egm --name graphdb-container -p 7200:7200 dhlabbasel/graphdb-free

up: build run


stop: ## Stop a running container
		docker container stop neo4jscript-container || true
		docker container stop neo4jdatabase-container || true
		docker container stop graphdb-container || true
		
exec:
	docker exec -i neo4jscript-container sh -c "python /scripts/init.py"
	
execpy2neo:
	docker exec -i neo4jscript-container sh -c "python /scripts/py2neoexample.py"