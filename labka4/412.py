import json
import sys

def diff(obj1, obj2, path=""):
    differences = []

    keys = set(obj1.keys()).union(obj2.keys())
    for key in keys:
        full_path = f"{path}.{key}" if path else key
        val1 = obj1.get(key, "<missing>")
        val2 = obj2.get(key, "<missing>")

        if isinstance(val1, dict) and isinstance(val2, dict):
            differences.extend(diff(val1, val2, full_path))
        elif val1 != val2:
            val1_json = json.dumps(val1, separators=(',', ':')) if val1 != "<missing>" else "<missing>"
            val2_json = json.dumps(val2, separators=(',', ':')) if val2 != "<missing>" else "<missing>"
            differences.append(f"{full_path} : {val1_json} -> {val2_json}")

    return differences

obj1 = json.loads(sys.stdin.readline())
obj2 = json.loads(sys.stdin.readline())

diffs = diff(obj1, obj2)
if diffs:
    for line in sorted(diffs):
        print(line)
else:
    print("No differences")