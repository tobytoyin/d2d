import re
from dataclasses import dataclass
from typing import List

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
    out = []
    link_type = "LINK"  # obisidian only has a single link type
    links_match = set(re.findall(ObsidianMarkdownRegex.links, doc))

    if not links_match:
        return out

    for link in links_match:
        # extract id within [[links]]
        extracted_link_id = _extract_link_id(link)

        # extract alias within [[links|alias]] into prop
        extracted_alias = re.findall("\|(.*)", link)[0]

        out.append(
            {
                "doc_id": extracted_link_id,
                "rel_type": link_type,
                "ref_text": extracted_alias,
            }
        )

    return out
