from . import neo4j


def get_plugin(plugin_name: str):
    plugins = {
        "neo4j": neo4j.ServiceCatalog,
    }
    return plugins.get(plugin_name)
