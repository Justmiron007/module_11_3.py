from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj)
    attributes = dir(obj)
    methods = []
    for i in attributes:
        if callable(getattr(obj, i)):
            methods.append(i)
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return info


number_info = introspection_info(42)
pprint(number_info)
