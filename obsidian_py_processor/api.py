import re

import markdown
import yaml
from model import Document
from processors import frontmatter_processor

test_file = '/Users/tobiasto/Desktop/master-notes/pages/snowflake/d-2023-07-27-14-33-24.md'



    
    

with open(test_file, 'r') as f:
    
    text = f.read()
    print(text)
    metadata = frontmatter_processor(text)
    print(metadata)
    # print(text)
    # doc = Document(text=markdown.markdown(text=text))
    # print(doc.text)

    
