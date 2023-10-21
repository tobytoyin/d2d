from d2d.contracts.document import DocumentRelations

from ._processor import links_processor


def source_reader(source) -> str:
    with open(source.path, "r") as f:
        text = f.read()
        return text


def link_extractions(source):
    text = source_reader(source)

    out = []
    links = links_processor(text)
    for link in links:
        doc_id = link.pop("rel_uid")
        rel_type = link.pop("rel_type")
        new_obj = {"rel_uid": doc_id, "rel_type": rel_type, "properties": link}
        out += [DocumentRelations(**new_obj)]
    return out
