from ..protocols._document_to_db import DocumentToDB
from .enums import Endpoints
from .mock import services as mock_services

# from .neo4j import services as neo4j_services

######
# Current `ConnectorServiceCatalog` is used to fetch the service
# that are implemented by each database/ sink connectors

# This requires implemented service by each connector to be:
# - registered within the `ServiceCatalog` within their own class using the service Enum
# -


class ServicesCatalog:
    @classmethod
    def get_service_endpoint(cls, dst: Endpoints):
        endpoints = {"mock": mock_services.ServiceCatalog}

        try:
            return endpoints.get(dst)
        except KeyError as err:
            raise KeyError(f"service endpoint {dst} doesn't exist.") from err

    @classmethod
    def document_to_database(cls, dst: Endpoints) -> DocumentToDB:
        """This reaches to the 'document_to_database' service implemented by connectors

        :param dst: _description_
        :type dst: ConnectionEndpoints
        :raises AttributeError: _description_
        :return: _description_
        :rtype: DocumentToDB
        """
        service_name = "document_to_database"
        endpoint = cls.get_service_endpoint(dst)
        try:
            return getattr(endpoint, service_name)
        except AttributeError as err:
            msg = f"{dst} doesn't have any implemented service:{service_name}"
            raise AttributeError(msg) from err
