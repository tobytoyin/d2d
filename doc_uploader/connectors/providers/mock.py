import logging


class MockConnector:
    def __init__(self, *args, **kwargs) -> None:
        self.driver = None

    def close(self):
        logging.debug("mock connector closed")

    def run(self, uow):
        logging.debug("mock connector session start")
        result = uow()
        logging.debug(f"mock uow results: {result}")

        self.close()
        return result
