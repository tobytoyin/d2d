from graphene import ObjectType, String


class Source(ObjectType):
    path = String(required=True)
    source_type = String(required=True)
