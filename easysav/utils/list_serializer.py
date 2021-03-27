def serialize_list(list):
    return '[' + ','.join(map(lambda item: str(item.to_dict()), list)) + ']'
