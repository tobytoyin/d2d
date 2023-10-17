# Doc Uploader 

## CLI Usage

```shell
python3 -m doc_uploader.cli  --src obsidian  --dst neo4j --files file1.md file2.md

# upload every from a subdirectory
find . -type f | \
grep <pattern> | \
xargs -I "{}" python3 -m doc_uploader.cli --src obsidian --dst neo4j --files "{}"

# using a diff set (e.g., git diff)
git diff --name-only --diff-filter=ACMRT | \
grep <pattern> | \
xargs -I "{}" python3 -m doc_uploader.cli --src obsidian --dst neo4j --files "{}"
```

## Overall Designs
![image](https://github.com/tobytoyin/document-graph-processor/assets/40096033/9535a883-c494-4cf8-951f-d371054f394d)


## Connectors Service Catalogs 
![image](https://github.com/tobytoyin/document-graph-processor/assets/40096033/0c4782da-b575-46f9-938c-41e4c70e8efb)

The service catalog at the connectors tasks provide: 
- available services within the tool
- abstraction of the structures of the different services, such that Tasks can interface with different Connectors implementations
- available services implemented within different Connectors (e.g., Neo4J graphs upload service, Relational DB upload service, PineconeDB embedding uploads)
