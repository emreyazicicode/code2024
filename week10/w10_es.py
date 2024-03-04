from datetime import datetime
from elasticsearch import Elasticsearch

#* Create a connection
es = Elasticsearch("http://localhost:9200")

#* Create a document/row/record to be inserted
doc = {
    "text": "Elasticsearch: cool. bonsai cool.",
}

#* Insert in into "test-index" 
#* INSERT "doc" INTO "test-index"
# resp = es.index(index="test-index", id=2, document=doc)
#es.indices.refresh(index="test-index")
#print(resp)

#* SELECT * FROM "test-index" WHERE "text" LIKE "emre"

resp = es.search(index="test-index", query={"match": {"text": {"query": "cool"}}})
#resp = es.search(index="test-index", query={"match_all": {}})
print("Got {} hits:".format(resp["hits"]["total"]["value"]))
for hit in resp["hits"]["hits"]:
    print(hit["_source"])

