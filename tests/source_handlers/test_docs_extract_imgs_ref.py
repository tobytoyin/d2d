# from pathlib import Path

# from pytest import fixture

# from doc_uploader.adapters.factory import create_document
# from doc_uploader.adapters.mock.image_ref_extractor import MockRefExtractor
# from doc_uploader.contracts.source import Source
# from doc_uploader.source_handlers.docs_extract_imgs_ref import DocumentsToImageSource


# @fixture
# def random_docs():
#     # create 10 randoms doc
#     source = Source(path=Path("."), source_type="mock", root=Path("home"))
#     return [create_document(source)]


# def test_endpoint(random_docs):
#     endpoint = DocumentsToImageSource(
#         documents=random_docs,
#         extractor=MockRefExtractor,
#     )
#     res = list(endpoint.image_sources())[0]

#     res_paths = set([str(r.path) for r in list(res)])
#     assert res_paths == set(["home/img1.png", "home/img2.png", "home/img3.png"])
