import asyncio
from typing import Callable

from d2d.contracts.documents import Document
from d2d.plugins.factory import get_plugin


class DocumentServicesDispatcher:
    @staticmethod
    def service_runner(
        document: Document,
        plugin_name: str | None = None,
        service_catalog=None,
        service_name: str | None = None,
        service_fn: Callable[[Document], None] | None = None,
    ):
        """
        This method would execute the service_function based on two approach:

        If the `service_fn` is provided, `document` would directly call on that function.\

        Otherwise, the service function would be retrieved based on `plugins.factory` and \
        retrieve the function based on given `plugin_name`, `service_name`.

        `service_catalog` uses a similar approach but skipped the need of using `plugin_name` to \
        retrieve `ServiceCatalog` object. Instead you directly pass that object into the dispatcher


        :param document: _description_
        :type document: Document
        :param plugin_name: The name of the plugin which implements a ServiceCatalog, defaults to None
        :type plugin_name: str | None, optional
        :param service: _description_, defaults to None
        :type service: _type_, optional
        :param service_name: \
            The callable name under the ServiceCatalog. \
            Ideally this would be `ServiceCatalog.<service_name>`, defaults to None
        :type service_name: str | None, optional
        :param service_fn: \
            A callable function that can be called directly, defaults to None
        :type service_fn: Callable[[Document], None], optional
        :return: _description_
        :rtype: _type_
        """
        if service_fn:
            service_fn(document)

        if not service_catalog:
            service_catalog = get_plugin(plugin_name=plugin_name)

        return getattr(service_catalog, service_name)(document)
