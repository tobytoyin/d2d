from ..processor import frontmatter_processor, links_processor


def test_links_extracted():
    contents = """
    This is a dummy md. This is my [[prefix/document-id-1|alias 1]].
    This is my [[document-id-2|alias 2]], and this can another line.
    This is a non alias links: [[document-id-3]]
    This is duplicated with the same [[path/document-id-4]].

    This is my image: ![[image-reference]]
    """.strip()

    links = links_processor(contents)

    expected = [
        {
            "rel_uid": "document-id-1",
            "rel_type": "LINK",
            "properties": {"ref_text": ["alias 1"]},
        },
        {
            "rel_uid": "document-id-2",
            "rel_type": "LINK",
            "properties": {"ref_text": ["alias 2"]},
        },
        {
            "rel_uid": "document-id-3",
            "rel_type": "LINK",
            "properties": {"ref_text": []},
        },
        {
            "rel_uid": "document-id-4",
            "rel_type": "LINK",
            "properties": {"ref_text": []},
        },
    ]

    assert all(l in expected for l in links)  # testing elements but not order


def test_no_links_extracted():
    contents = """
    ---
    type: test
    name: my-dummy-doc
    ---

    This is my image: ![[image-reference]]
    """

    links = links_processor(contents)
    expected = []

    assert links == expected


def test_metadata_extracted():
    contents = """
    ---
    type: test
    name: my-dummy-doc
    ---

    This is a dummy md


    ---
    Line breaker shouldn't be extracted as meta data

    ---

    Another line
    """
    contents = [line.strip() for line in contents.split("\n")]
    contents = "\n".join(contents)

    metadata = frontmatter_processor(contents)
    expected = {"doc_type": "test", "properties": {"name": "my-dummy-doc"}}

    assert metadata == expected


def test_no_metadata_extracted():
    contents = """
    This is a dummy md
    """

    metadata = frontmatter_processor(contents)
    expected = {"doc_type": "unknown"}
    assert metadata == expected
