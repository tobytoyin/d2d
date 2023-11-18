import importlib

a = importlib.import_module("d2d.providers.obsidian")
print(getattr(a, "TaskCatalog").metadata)
