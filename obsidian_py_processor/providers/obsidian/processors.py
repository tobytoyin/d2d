import re
from dataclasses import dataclass

import yaml


@dataclass
class ObsidianMarkdownRegex:
    frontmatter = f'---\n((.|\n)+?)\n---'
    links = r'(?<!!)\[\[(.*)\]\]'


def frontmatter_processor(doc: str) -> str:
    """convert frontmatter string into metada dict"""
    metayamml_match = re.search(ObsidianMarkdownRegex.frontmatter, doc)

    if not metayamml_match:
        return {}

    yamml_str = metayamml_match.groups()[0]

    metadata = yaml.safe_load(yamml_str)

    return metadata


def links_processor(doc: str) -> set:
    """extract all mentioned links

    Links such as would extract into:
    - [[document-id|alias]] --> "document-id"
    - [[document-id]] --> "document-id"
    """
    out = set()
    links_match = set(re.findall(ObsidianMarkdownRegex.links, doc))

    if not links_match:
        return out

    for link in links_match:
        extracted_link_id = re.sub(ObsidianMarkdownRegex.links, '\1', link)  # extract id within [[links]]
        extracted_link_id = re.sub('\|.*', '', extracted_link_id)  # remove alias

        out.add(extracted_link_id)

    return out
