import re

import markdown
import yaml
from base.db_models import GraphDocumentModel
from connectors.neo4j import Neo4JConnector, Neo4JUoW
from nlp.sentence_embed import SentenceEmbedding

# from model import Document
# from processors import frontmatter_processor
from providers.obsidian.models import ObsidianDocument
from providers.obsidian.processors import frontmatter_processor

test_file = 'tests/providers/obsidian/test_docs/doc_with_frontmatter.md'

doc = ObsidianDocument(path=test_file)
print(doc.metadata.model_dump())

db_model = GraphDocumentModel(document=doc)
print(GraphDocumentModel(document=doc).record)

adapter = Neo4JUoW(db_model)

neo4j.run(adapter.update_or_create_node)
neo4j.run(adapter.update_or_create_relationships)
