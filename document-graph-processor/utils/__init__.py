def no_quotes_object(obj: dict) -> str: 
    """convert python dict object to object without quoted key
    """
    prop_strings = []
    for k, v in obj.items():
        prop_strings.append(f'{k}: "{v}"')
    return '{' + ','.join(prop_strings) + '}'