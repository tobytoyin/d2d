import re
from dataclasses import dataclass
from typing import Set

import yaml


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


def links_processor(doc: str) -> Set[dict]:
    """extract all mentioned links

    Links such as would extract into:
    - [[document-id|alias]] --> "document-id"
    - [[document-id]] --> "document-id"

    """
    out = set()
    link_type = "LINK"  # obisidian only has a single link type
    links_match = set(re.findall(ObsidianMarkdownRegex.links, doc))

    if not links_match:
        return out

    for link in links_match:
        # extract id within [[links]]
        extracted_link_id = re.sub(ObsidianMarkdownRegex.links, "\1", link)

        # extract alias within [[links|alias]] into prop
        extracted_alias = re.findall("\|(.*)", extracted_link_id)[0]

        extracted_link_id = re.sub("\|.*", "", extracted_link_id)  # remove alias
        extracted_link_id = re.sub("#.*", "", extracted_link_id)  # remove header references

        out.add(
            {
                "doc_id": extracted_link_id,
                "rel_type": link_type,
                "ref_text": extracted_alias,
            }
        )

    return out
