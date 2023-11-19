import argparse
import asyncio
from typing import TypeAlias

from d2d.plugins.neo4j.to_embedding import DocumentToN4JEmbedding
from d2d.tasks.document_composer import DocumentComposer

IS_COMPLETED: TypeAlias = bool


class DocumentToVsAPI:
    @staticmethod
    def async_run(payload):
        asyncio.run(DocumentToVsAPI.run(payload))

    @staticmethod
    async def run(payload):
        documents = DocumentComposer().run(payload)

        async with asyncio.TaskGroup() as tg:
            for doc in documents:
                asyncio.create_task(DocumentToVsAPI.doc_to_graph_runner(doc))

    @staticmethod
    async def doc_to_graph_runner(document) -> IS_COMPLETED:
        process = DocumentToN4JEmbedding()
        process.update_or_create_embedding(document)

        return True
