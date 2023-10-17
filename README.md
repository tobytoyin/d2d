# Doc Uploader 

## Overall Designs
![image](https://github.com/tobytoyin/document-graph-processor/assets/40096033/9535a883-c494-4cf8-951f-d371054f394d)

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
