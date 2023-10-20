# define the protocols and source types in this file here for registration
from .service_functions import link_extractions, source_reader


class SourceHandlers:
    SOURCE_READER = source_reader
    LINK_PROCESSOR = link_extractions
    META_PROCESSOR = None
