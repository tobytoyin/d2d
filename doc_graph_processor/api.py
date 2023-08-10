import re

import markdown
import yaml
from base.db_models import GraphDocumentModel
# from model import Document
# from processors import frontmatter_processor
from providers.obsidian.models import ObsidianDocument
from providers.obsidian.processors import frontmatter_processor

test_file = 'tests/providers/obsidian/test_docs/doc_with_frontmatter.md'

doc = ObsidianDocument(path=test_file)
print(doc.metadata.model_dump())


print(GraphDocumentModel(document=doc).record)
    
# with open(test_file, 'r') as f:
    
#     text = f.read()
#     metadata = frontmatter_processor(text)
#     # print(text)
#     doc = Document(text=markdown.markdown(text=text))
#     print(doc.text)

    
