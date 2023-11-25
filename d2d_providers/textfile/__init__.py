# follows the services.SourceIO interface
from .processor import frontmatter_processor, links_processor


class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        with open(d["path"], "r") as f:
            return f.read()

    @staticmethod
    def uid_gen(d):
        return str(d["path"]).split("/")[-1].split(".")[0]
