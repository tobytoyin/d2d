from doc_uploader.api.uploader import Uploader
from doc_uploader.app.profile import Profile
from doc_uploader.databases.base_models import GraphDocumentModel
from doc_uploader.doc_handlers.factory import DocHandlerFactory

test_file = 'tests/doc_handlers/obsidian/test_docs/doc_with_frontmatter.md'
uploader = Uploader(profile=Profile())

doc = DocHandlerFactory.obsidian(test_file)

print(doc.metadata.model_dump())

db_model = GraphDocumentModel(document=doc)
print(GraphDocumentModel(document=doc).record)

uploader.neo4j_uploader(db_model)
