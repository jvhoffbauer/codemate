def get_graphql_question_discussion_edges(
    *,
    settings: Settings,
    after: Union[str, None] = None,
):
    data = get_graphql_response(
        settings=settings,
        query=discussions_query,
        after=after,
        category_id=questions_category_id,
    )
    graphql_response = DiscussionsResponse.model_validate(data)
    return graphql_response.data.repository.discussions.edges