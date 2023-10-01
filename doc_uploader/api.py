from app.logger import setup_custom_logger

from doc_uploader.connectors.factory import get_connector
from doc_uploader.doc_handlers.factory import create_document
from doc_uploader.services.db_handler.factory import get_uow

logger = setup_custom_logger("root")


class UploaderAPI:
    def __init__(self, source: str, destination: str, files: list) -> None:
        self.source = source
        self.destination = destination
        self.files = iter(files)

    def upload(self):
        conn = get_connector(self.destination)

        for f in self.files:
            document = create_document(self.source, f)
            # TODO find a way to swtich between different models
            db_uow = get_uow(self.destination, document)
            conn.run(db_uow.update_or_create_document)
            conn.run(db_uow.update_or_create_relationships)
            print(f"uploaded - {f}")
