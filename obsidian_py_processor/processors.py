import re

import yaml


def frontmatter_processor(doc: str) -> str: 
    """convert frontmatter string into metada dict"""
    metayamml_match = re.search('---\n((.|\n)+?)\n---', doc)
    
    if not metayamml_match:
        return {}

    yamml_str = metayamml_match.groups()[0]

    metadata = yaml.safe_load(yamml_str)
    
    return metadata

