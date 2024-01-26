- Generates an OpenAPI v3 specification from FastAPI routes and models using Pydantic's JSON schema generation feature.
- Defines `methods_spec`, `schemas_spec`, and `errors_by_code` dictionaries to store information about each endpoint's parameters, results, tags, errors, and data types.
- Loops through all registered routes (of type `MethodRoute`) and extracts relevant metadata such as name, summary, parameters, result model, tags, and errors.
- Creates a dictionary representation of each endpoint's operation object (i.e., its HTTP request/response behavior).
- Merges parameter and result schemas into their respective definitions within `schemas_spec`.
- Groups errors by their status codes and creates separate error specifications for them.
- Returns a complete OpenAPI v3 specification that includes the API version, title, server URLs, operations, components, and error definitions.