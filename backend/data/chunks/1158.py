def create_comment(*, settings: Settings, discussion_id: str, body: str):
    data = get_graphql_response(
        settings=settings,
        query=add_comment_mutation,
        discussion_id=discussion_id,
        body=body,
    )
    response = AddCommentResponse.parse_obj(data)
    return response.data.addDiscussionComment.comment