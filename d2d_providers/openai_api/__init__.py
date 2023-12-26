import json

from openai import OpenAI


# follows the services.SourceTasks interface
class TaskCatalog:
    @staticmethod
    def embedding(text: str, api_key: str):
        client = OpenAI(api_key=api_key)
        callback = client.embeddings
        res = callback.create(
            model="text-embedding-ada-002",
            input=text,
            encoding_format="float",
        )

        return {
            "vector": res.data[0].embedding,
            "source": "openai",
            "model": "text-embedding-ada-002",
            "dimension": 1536,
        }

    @staticmethod
    def named_entity_relations(text: str, api_key: str):
        client = OpenAI(api_key=api_key)
        callback = client.chat.completions

        prompt_template = """
        You are a data scientist who wishes to create knowledge graph. Your task
        is to:
        - extract about 10 named entities and relationships from a piece of text
        - only extract important entities and keywords but avoid common noun phrases

        When an entity is extracted, you should output them following the below rules:
        - named entity structure  with: {"id": ENTITY_ID, "type": ENTITY_TYPE, "properties": PROPERTIES}
        - ENTITY_ID should prioritise in noun phrases, named entities, or keywords
        - ENTITY_TYPE should be in CamelCase without spaces
        - ENTITY_TYPE should be different from ENTITY_ID and use noun that represents into general category, i.e., Technology, Company, Location
        - relationships structures with {"root": ENTITY_ID_ROOT, "type": RELATION_TYPE, "target": ENTITY_ID_OTHER, "properties": PROPERTIES}
        - RELATION_TYPE should limit to verbs; verbs are in present tense; verbs phrases are joined with _
        - RELATION_TYPE should have no special symbols other an "_"; it should be in CAPITAL_CASE
        - ENTITY_ID_ROOT and ENTITY_ID_OTHER can only be extracted named entity ENTITY_ID

        You should only output the result as JSON object.

        Example:
        content: Alice lawyer and is 25 years old and Bob is her roommate since 2001. Bob works as a journalist. Alice owns a the webpage www.alice.com and Bob owns the webpage www.bob.com.
        {
            "entities": [
                {"id": "alice", "type": "Person", "properties": {"age": "25", "occupation": "lawyer", "name":"Alice"}},
                {"id": "bob", "type": "Person", "properties": {"occupation": "journalist", "name": "Bob"}},
                {"id": "alice.com", "type": "Webpage", "properties": {"url": "www.alice.com"}}
            ],
            "relations": [
                {"root": "alice", "type": "IS", "target": "bob", "properties": {"start": "2021", "relation": "roommate"}}
                {"root": "alice", "type": "OWN", "target": "alice.com", "properties": {}}
            ]
        }
        """.strip()

        completion = callback.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_template},
                {"role": "user", "content": text},
            ],
        )
        print(completion.choices[0].message.content)
        payload = json.loads(completion.choices[0].message.content)

    

        return {
            **payload,
            "source": "openai",
            "model": "gpt-3.5-turbo",
        }
