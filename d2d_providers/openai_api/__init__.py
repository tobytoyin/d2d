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
            "vector": tuple(res.data[0].embedding),
            "source": "openai",
            "model": "text-embedding-ada-002",
        }


#     def named_entity_relations(text: str, api_key: str):
#         client = OpenAI()
#         callback = client.chat.completions
#         callback.api_key = api_key

#         prompt_template = """
#         You are a data scientist who wishes to create knowledge graph. Your task
#         is to:
#         - extract named entity and relationships from a piece of text
#         - only extract important entity but avoid common nouns

#         When an entity is extracted, you should output them following the below rules:
#         - named entity structure  with: [ENTITY_ID, TYPE, PROPERTIES]
#         - relationships structures with [ENTITY_ID_ROOT, RELATIONSHIP, ENTITY_ID_OTHER, PROPERTIES]
#         - RELATIONSHIP should be verb phrase only and contains no tenses
#         - ENTITY_ID_ROOT and ENTITY_ID_OTHER can only be extracted named entity ENTITY_ID

#         You should only output the result as JSON object.

#         Example:
#         content: Alice lawyer and is 25 years old and Bob is her roommate since 2001. Bob works as a journalist. Alice owns a the webpage www.alice.com and Bob owns the webpage www.bob.com.
#         {
#             "nodes": ["alice", "Person", {"age": 25, "occupation": "lawyer", "name":"Alice"}], ["bob", "Person", {"occupation": "journalist", "name": "Bob"}], ["alice.com", "Webpage", {"url": "www.alice.com"}], ["bob.com", "Webpage", {"url": "www.bob.com"}],
#             "relationships": ["alice", "IS_ROOMMATE", "bob", {"start": 2021}], ["alice", "OWN", "alice.com", {}], ["bob", "OWN", "bob.com", {}]
#         }
#         """.strip()

#         completion = callback.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": prompt_template},
#                 {"role": "user", "content": text},
#             ],
#         )

#         return completion.choices[0].message.content
