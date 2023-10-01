from doc_uploader.app.profile import Profile
from doc_uploader.common.factory import FactoryRegistry


class ConnectorsContainer(FactoryRegistry):
    _map = {}
    import_pattern = "connectors/providers/*.py"


def get_profile(connector_name: str):
    profile = Profile()
    return profile.storage(connector_name)


def get_connector(name: str, *args, **kwargs):
    connector = ConnectorsContainer.get(name=name)
    # profile = get_profile(name)
    return connector()
