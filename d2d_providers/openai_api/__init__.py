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
        You are a data scientist who wishes to create knowledge graph. Your task is to:
        - extract about 10 named entities relationships from a piece of text
        - named entities should be important entities or keywords and avoid common noun phrases

        When an entity is extracted, you should output them following the below rules:
        - named entity are structured: {"id": ENTITY_ID, "type": ENTITY_TYPE, "properties": PROPERTIES}
        - relationships ared structured: {"root": ENTITY_ID_ROOT, "type": RELATION_TYPE, "target": ENTITY_ID_OTHER, "properties": PROPERTIES}
        - if possible, replace ENTITY_ID with a similar term, e.g., "data base" becomes "database", "mobile devices" becomes "mobile phone"
        - if possible, replace plural ENTITY_ID to singular
        - ENTITY_TYPE should be in CamelCase without spaces    
        - ENTITY_TYPE should be output as a general term or a category, i.e., Technology, Company, Location, Person
        - RELATION_TYPE should limit to verbs; verbs are in present tense; should be written in active voice
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
                {"root": "alice", "type": "OWNS", "target": "alice.com", "properties": {}}
            ]
        }
        """.strip()

        completion = callback.create(
            model="gpt-3.5-turbo-1106",
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
            "model": "gpt-3.5-turbo-1106",
        }
