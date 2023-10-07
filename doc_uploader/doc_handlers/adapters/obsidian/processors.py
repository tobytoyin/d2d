import re
from dataclasses import dataclass
from typing import List

import yaml

from doc_uploader.utils import append_dict_iterable


@dataclass
class ObsidianMarkdownRegex:
    frontmatter = f"---\n((.|\n)+?)\n---"
    links = r"(?<!!)\[\[(.*)\]\]"


def frontmatter_processor(doc: str) -> dict:
    """convert frontmatter string into metada dict"""
    metayamml_match = re.search(ObsidianMarkdownRegex.frontmatter, doc)

    if not metayamml_match:
        return {"doc_type": "unknown"}

    yamml_str = metayamml_match.groups()[0]

    metadata = yaml.safe_load(yamml_str)
    metadata["doc_type"] = metadata.pop("type")
    return metadata


def _extract_link_id(link_str: str) -> str:
    extracted_link_id = re.sub(ObsidianMarkdownRegex.links, "\1", link_str)
    extracted_link_id = re.sub("\|.*", "", extracted_link_id)  # remove alias
    extracted_link_id = re.sub("#.*", "", extracted_link_id)  # remove header references
    return extracted_link_id


def links_processor(doc: str) -> List[dict]:
    """extract all mentioned links

    Links such as would extract into:
    - [[document-id|alias]] --> "document-id"
    - [[document-id]] --> "document-id"

    """
    collection = {}
    link_type = "LINK"  # obisidian only has a single link type
    links_match = set(re.findall(ObsidianMarkdownRegex.links, doc))

    if not links_match:
        return []

    for link in links_match:
        # extract id within [[links]]
        extracted_link_id = _extract_link_id(link)

        # extract alias within [[links|alias]] into prop
        extracted_alias = re.findall("\|(.*)", link)

        update_obj = {
            "doc_id": extracted_link_id,
            "rel_type": link_type,
            "ref_text": set(extracted_alias) if extracted_alias else set(),
        }

        # find if the collection contains the relational dict
        # if there's one, append the new fields into the existing fields
        # if there's none, put the new object into the collection
        hash_key = f"{extracted_link_id}-{link_type}"
        target = collection.get(hash_key)

        if target:
            new_obj = append_dict_iterable(target, update_obj, append_keys=["ref_text"])
            collection[hash_key] = new_obj
        else:
            collection[hash_key] = update_obj

    return list(collection.values())
