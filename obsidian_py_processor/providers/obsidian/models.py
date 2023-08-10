from dataclasses import dataclass

from models import Document
from providers.obsidian import processors


class ObsidianDocument(Document):
    metadata_processor = staticmethod(processors.frontmatter_processor)
    
    def id_resolver(self):
        # use the filename as id
        return self.path.split('/')[-1].split('.')[0]
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()