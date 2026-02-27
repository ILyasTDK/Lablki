import json

def patch_update(source, patch):
    for key, value in patch.items():
        if value is None:
            source.pop(key, None)
        elif key in source and isinstance(source[key], dict) and isinstance(value, dict):
            patch_update(source[key], value)
        else:
            source[key] = value
    return source

source = json.loads(input())
patch = json.loads(input())
result = patch_update(source, patch)
print(json.dumps(result, sort_keys=True, separators=(',', ':')))