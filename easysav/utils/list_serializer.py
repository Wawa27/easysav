def serialize_list(list):
    return map(lambda item: str(item.to_dict()), list)
