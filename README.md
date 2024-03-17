# Doc Uploader 

## CLI Usage

```shell
python3 -m d2d.cli.main \
--source_spec '{"provider": "someProviderName"}' \
--tasks metadata='{"provider": "someProviderName"}' relations='{"provider": "someProviderName"}' \
--document_services '{"plugin_name": "neo4j","service_name": "update_or_create_document"}' \
--files file1.txt file2.txt file3.txt
```
