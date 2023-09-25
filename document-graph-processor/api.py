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

# connection
with open("profile.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
print(config)        

neo4j = Neo4JConnector(uri=config['storages']['neo4j']['uri'], 
                       username=config['storages']['neo4j']['username'], 
                       password=config['storages']['neo4j']['password'])

test_file = 'tests/providers/obsidian/test_docs/doc_with_frontmatter.md'

doc = ObsidianDocument(path=test_file)
print(doc.metadata.model_dump())

db_model = GraphDocumentModel(document=doc) 
print(GraphDocumentModel(document=doc).record)

adapter = Neo4JUoW(db_model)

neo4j.run(adapter.update_or_create_node)
neo4j.run(adapter.update_or_create_relationships)



# emb = SentenceEmbedding(doc.contents).doc_embeddings
# print(emb)
# print(emb.shape)
    
# with open(test_file, 'r') as f:
    
#     text = f.read()
#     metadata = frontmatter_processor(text)
#     # print(text)
#     doc = Document(text=markdown.markdown(text=text))
#     print(doc.text)

    
