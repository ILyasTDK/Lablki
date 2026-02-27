import importlib

n = int(input())
for _ in range(n):
    module_path, attr = input().split()
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(module, attr):
        print("ATTRIBUTE_NOT_FOUND")
    elif callable(getattr(module, attr)):
        print("CALLABLE")
    else:
        print("VALUE")