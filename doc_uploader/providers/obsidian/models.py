from doc_uploader.base.doc_models import BaseDocument

from .processors import frontmatter_processor, links_processor


class ObsidianDocument(BaseDocument):
    metadata_processor = staticmethod(frontmatter_processor)
    relations_processor = staticmethod(links_processor)

    def id_resolver(self):
        # use the filename as id
        return self.path.split('/')[-1].split('.')[0]

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()
