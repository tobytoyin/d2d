from . import aws, neo4j


def get_plugin(plugin_name: str):
    plugins = {
        "neo4j": neo4j.ServiceCatalog,
        "aws": aws.ServiceCatalog,
    }
    return plugins.get(plugin_name)
