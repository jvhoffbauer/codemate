- Retrieves a list of pull requests from GitHub using GraphQL API with optional pagination (specified by `after`)
- Parses the response and returns an iterable containing tuples representing each pull request as an edge object in the form of (node, cursor) pairs