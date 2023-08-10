from base.doc_models import Document
from providers.obsidian import processors


class ObsidianDocument(Document):
    metadata_processor = staticmethod(processors.frontmatter_processor)
    relations_processor = staticmethod(processors.links_processor)
    
    def id_resolver(self):
        # use the filename as id
        return self.path.split('/')[-1].split('.')[0]
    
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()