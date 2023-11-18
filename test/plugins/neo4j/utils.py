from d2d.plugins.neo4j.mixin import GraphDBMixin


def reset_neo4j():
    neo4j = GraphDBMixin()
    neo4j.driver.execute_query("MATCH (n) DETACH DELETE n")
    return
