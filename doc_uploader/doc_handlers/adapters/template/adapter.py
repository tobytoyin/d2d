from doc_uploader.doc_handlers.factory import DocumentAdapterContainer
from doc_uploader.doc_handlers.interfaces import DocumentAdapter

# adapter.py - is the lookup folder for the factory
# define new Adapters using the below template

# Logics to implement the methods of `DocumentAdapter` can be written herein\
#   or preferablly inside `./processors.py`


# @Registry.register(name="my_adapter")
class MyAdapater(DocumentAdapter):
    ...
