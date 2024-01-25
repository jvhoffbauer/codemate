def get_graphql_pr_edges(*, settings: Settings, after: Union[str, None] = None):
    data = get_graphql_response(settings=settings, query=prs_query, after=after)
    graphql_response = PRsResponse.model_validate(data)
    return graphql_response.data.repository.pullRequests.edges