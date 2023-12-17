from pytest import fixture


@fixture
def doc1():
    with open("d2d_providers/obsidian/tests/documents/image_file.md", "r") as f:
        return f.read()
