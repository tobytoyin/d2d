from openai import OpenAI


# follows the services.SourceTasks interface
class TaskCatalog:
    provider_name = "openai"

    @staticmethod
    def embedding(text: str, api_key: str):
        client = OpenAI()
        callback = client.embeddings
        callback.api_key = api_key
        res = callback.create(
            model="text-embedding-ada-002",
            input=text,
            encoding_format="float",
        )

        return {"embedding": res.data[0].embedding}

    def named_entity_relations(text: str, api_key: str):
        client = OpenAI()
        callback = client.chat.completions
        callback.api_key = api_key

        prompt_template = """
        You are a data scientist who wishes to create knowledge graph. Your task
        is to:
        - extract named entity and relationships from a piece of text
        - only extract important entity but avoid common nouns

        When an entity is extracted, you should output it in a form of: [ENTITY_ID, TYPE, PROPERTIES]
        and extracted relationship in a form of [ENTITY_ID_ROOT, RELATIONSHIP, ENTITY_ID_OTHER, PROPERTIES].
        You should only output the result as JSON object.

        Example:
        content: Alice lawyer and is 25 years old and Bob is her roommate since 2001. Bob works as a journalist. Alice owns a the webpage www.alice.com and Bob owns the webpage www.bob.com.
        {
            "nodes": ["alice", "Person", {"age": 25, "occupation": "lawyer", "name":"Alice"}], ["bob", "Person", {"occupation": "journalist", "name": "Bob"}], ["alice.com", "Webpage", {"url": "www.alice.com"}], ["bob.com", "Webpage", {"url": "www.bob.com"}],
            "relationships": ["alice", "roommate", "bob", {"start": 2021}], ["alice", "owns", "alice.com", {}], ["bob", "owns", "bob.com", {}]
        }
        """.strip()

        completion = callback.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_template},
                {"role": "user", "content": text},
            ],
        )

        return completion.choices[0].message.content
