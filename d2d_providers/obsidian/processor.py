import re
from dataclasses import dataclass
from typing import List

import yaml

# from .utils import append_dict_iterable


@dataclass
class MdRegex:
    frontmatter = r"^---\s+((.|\n)+?)\n---\s+"
    frontmatter_section = r"^---\s+(?s:.+?)\s+---\s+"
    links = r"(?<!!)\[\[(.*)\]\]"
    render_ref = r"!\[\[(.+?)(?:\|.+?)?\]\]"
    # capture entire ![[...]] for images
    image_ref = r"(!\[\[(.+?(?:png|jpg))(?:\|.+?)?\]\])"


def inner_content_extraction(doc: str) -> str:
    return re.sub(MdRegex.frontmatter_section, "", doc.strip())


def frontmatter_processor(doc: str) -> dict:
    """convert frontmatter string into metada dict"""
    metayamml_match = re.search(MdRegex.frontmatter, doc.strip())

    if not metayamml_match:
        return {"doc_type": "unknown"}

    yamml_str = metayamml_match.groups()[0]

    metadata = yaml.safe_load(yamml_str)

    return {
        "doc_type": metadata.pop("type"),
        "properties": metadata,
    }


def _extract_link_id(link_str: str) -> str:
    extracted_link_id = re.sub(MdRegex.links, "\1", link_str)
    extracted_link_id = re.sub("\|.*", "", extracted_link_id)  # remove alias
    extracted_link_id = re.sub("#.*", "", extracted_link_id)  # remove header references
    extracted_link_id = re.sub("\\", "", extracted_link_id)  # remove symbol break within table
    extracted_link_id = extracted_link_id.split("/")[-1]  # remove filepath if any
    return extracted_link_id


def links_processor(doc: str) -> List[dict]:
    """extract all mentioned links

    Links such as would extract into:
    - [[document-id|alias]] --> "document-id"
    - [[document-id]] --> "document-id"

    """
    collection = {}
    link_type = "LINK"  # obisidian only has a single link type
    links_match = set(re.findall(MdRegex.links, doc))

    if not links_match:
        return []

    for link in links_match:
        # extract id within [[links]]
        extracted_link_id = _extract_link_id(link)

        # extract alias within [[links|alias]] into prop
        extracted_alias = re.findall("\|(.*)", link)

        update_obj = {
            "rel_uid": extracted_link_id,
            "rel_type": link_type,
            "properties": {
                "ref_text": extracted_alias if extracted_alias else [],
            },
        }

        # find if the collection contains the relational dict
        # if there's one, append the new fields into the existing fields
        # if there's none, put the new object into the collection
        hash_key = f"{extracted_link_id}-{link_type}"
        target = collection.get(hash_key)

        # if target:
        #     new_obj = append_dict_iterable(target, update_obj, append_keys=["ref_text"])
        #     collection[hash_key] = new_obj
        # else:
        collection[hash_key] = update_obj

    return list(collection.values())


def image_extraction(doc: str) -> List[str]:
    render_refs = set(re.findall(MdRegex.render_ref, doc))

    def _filter_img_ext(e: str):
        if e.split(".")[-1] in ["png", "jpg"]:
            return e

    return list(filter(_filter_img_ext, render_refs))


def image_ref_to_url(doc: str, url_prefix: str) -> str:
    sub_url_regex = rf'[<img src="{url_prefix}\2">]()'
    result = re.sub(MdRegex.image_ref, sub_url_regex, doc)
    return result
