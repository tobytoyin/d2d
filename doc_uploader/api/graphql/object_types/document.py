from graphene import Dynamic, Field, List, ObjectType, String


class DocumentMetadata(ObjectType):
    doc_type = String(required=True)

    def resolve_doc_type(root, info, type="document"):
        return type


class DocumentContent(ObjectType):
    contents = String(required=True)
    # bytes = String(required=True)


class DocumentRelations(ObjectType):
    rel_uid = String(required=True)
    rel_type = String(required=True)


# class Document(ObjectType):
#     uid = String(required=True)
#     metadata = Field(DocumentMetadata)

#     def resolve_metadata(root, info):
#         return
