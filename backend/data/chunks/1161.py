def get_graphql_issue_edges(*, settings: Settings, after: Union[str, None] = None):
    data = get_graphql_response(settings=settings, query=issues_query, after=after)
    graphql_response = IssuesResponse.model_validate(data)
    return graphql_response.data.repository.issues.edges