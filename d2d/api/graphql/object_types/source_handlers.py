from pathlib import Path

from graphene import List, ObjectType, String

from d2d.adapters.factory import get_adapter_service
from d2d.api.graphql.object_types.document import DocumentRelations
from d2d.contracts.source import Source


class SourceHandlers(ObjectType):
    """Query Schema for Adapter's Service Functions:

    type Query {
        relations(path: String!, sourceType: String!): [ DocumentRelations ]!
        metadata(path: String!, sourceType: String!): DocumentMetadata!

    }
    """

    relations = List(
        DocumentRelations,
        path=String(required=True),
        source_type=String(required=True),
        required=True,
    )

    def resolve_relations(root, info, path, source_type):
        source = Source(path=Path(path), source_type=source_type)
        service_fn = get_adapter_service(
            source=source,
            service_name="relations_extraction",
        )
        relations = service_fn(source)

        # map module type to ObjectType
        results = []
        for relation in relations:
            tmp = DocumentRelations(
                rel_uid=relation.rel_uid,
                rel_type=relation.rel_type,
            )
            results.append(tmp)

        return results


if __name__ == "__main__":
    import json

    from graphene import Schema

    schema = Schema(query=SourceHandlers)

    path = "/Users/chun.yin.to/Projects/document-graph-processor/tests/test_docs/doc_with_internal_links.md"
    source_type = "obsidian"

    query_str = """
    query getDocument($path: String!, $sourceType: String!) {
        relations(path: $path, sourceType: $sourceType) {
            relUid
            relType
        }
    }
    """

    result = schema.execute(
        query_str,
        variables={"path": path, "sourceType": source_type},
    )
    print(json.dumps(result.data))
