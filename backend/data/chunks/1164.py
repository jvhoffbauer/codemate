def get_graphql_sponsor_edges(*, settings: Settings, after: Union[str, None] = None):
    data = get_graphql_response(settings=settings, query=sponsors_query, after=after)
    graphql_response = SponsorsResponse.model_validate(data)
    return graphql_response.data.user.sponsorshipsAsMaintainer.edges