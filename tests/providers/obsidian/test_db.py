from neo4j import GraphDatabase

uri = "neo4j+s://ae48b625.databases.neo4j.io"
driver = GraphDatabase.driver(uri, auth=("neo4j", "jqUuhsUmBYq7CA7GZ5avmT0DIzHJq"))
print(driver)
driver.close()  # close the driver object