# Doc Uploader 

## CLI Usage

```shell
python3 -m d2d.cli.main \
--source_spec '{"provider": "someProviderName"}' \
--tasks metadata='{"provider": "someProviderName"}' relations='{"provider": "someProviderName"}' \
--document_services '{"plugin_name": "neo4j","service_name": "update_or_create_document"}' \
--files file1.txt file2.txt file3.txt
```

## Overall Designs
<img width="1108" alt="image" src="https://github.com/tobytoyin/document-graph-processor/assets/40096033/d3332a04-6c81-49e9-86e7-d370fa1b3dc3">


## Connectors Service Catalogs 
![image](https://github.com/tobytoyin/document-graph-processor/assets/40096033/0c4782da-b575-46f9-938c-41e4c70e8efb)

The service catalog at the connectors tasks provide: 
- available services within the tool
- abstraction of the structures of the different services, such that Tasks can interface with different Connectors implementations
- available services implemented within different Connectors (e.g., Neo4J graphs upload service, Relational DB upload service, PineconeDB embedding uploads)
