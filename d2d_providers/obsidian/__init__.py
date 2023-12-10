# follows the services.SourceIO interface
from .processor import (
    frontmatter_processor,
    image_extraction,
    inner_content_extraction,
    links_processor,
)


class SourceCatalog:
    @staticmethod
    def source_text(d: dict):
        with open(d["path"], "r") as f:
            return f.read()

    @staticmethod
    def metadata(d):
        return {
            "uid": str(d["path"]).split("/")[-1].split(".")[0],
        }


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def metadata(text):
        return frontmatter_processor(text)

    @staticmethod
    def relations(text):
        return {"items": links_processor(text)}

    @staticmethod
    def content(text):
        content = inner_content_extraction(text)

        return {
            "text": content,
            "codec": "markdown",
        }

    @staticmethod
    def obj_refs(text, prefix=""):
        img_refs = image_extraction(text)

        return {
            "paths": img_refs,
            "prefix": prefix,
        }
