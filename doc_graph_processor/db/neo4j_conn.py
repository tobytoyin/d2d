from neo4j import GraphDatabase


class Neo4JConnector:
    def __init__(self, uri, username, password) -> None:
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        
    # def __enter__(self):
    #     session = 
    #     self.session = session
    #     return self.session

    # def __exit__(self, exc_type, exc_value, exc_tb):
    #     # methods that could exec in finally block
    #     self.session.close()
    #     return True
    



n4j = Neo4JConnector("neo4j+s://ae48b625.databases.neo4j.io", "neo4j", "jqUuhsUmBYq7CA7GZ5avmT0DIzHJq-SL3nN1gYEYfcQ")
n4j.driver.execute_query("CREATE (n:Person {name: 'Andy', title: 'Developer'})")

n4j.driver.close()
# with n4j.driver.session() as session: 
#     print(session)
#     result = session.execute_query()
#     print(result)
#     result.consume()
#     print(result)
# print(driver)
# driver.close()  # close the driver object