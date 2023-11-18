`protocols/` contains all the abstract process of a single workflow
`adapters/` contains all the processor for different document's source to convert a `Source` into `Document`. 
`services/` contains all the Service function that consume a `Document` and process it to downstream plugins:
    - `connectors/services` - service implementation on how specific connector handle the services