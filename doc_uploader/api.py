from doc_uploader.connectors.factory import get_connector
from doc_uploader.doc_handlers.factory import create_document
from doc_uploader.services.db_handler.factory import get_uow

test_file = "tests/doc_handlers/obsidian/test_docs/doc_with_frontmatter.md"

document = create_document("obsidian", path=test_file)
db_uow = get_uow("neo4j", document)


# uploader = Uploader(profile=Profile())

# doc = DocHandlerFactory.obsidian(test_file)

# print(doc.metadata.model_dump())

# db_model = GraphDocumentModel(document=doc)
# print(GraphDocumentModel(document=doc).record)

# uploader.neo4j_uploader(db_model)
