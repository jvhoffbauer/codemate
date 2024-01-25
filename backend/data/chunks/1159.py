def update_comment(*, settings: Settings, comment_id: str, body: str):
    data = get_graphql_response(
        settings=settings,
        query=update_comment_mutation,
        comment_id=comment_id,
        body=body,
    )
    response = UpdateCommentResponse.parse_obj(data)
    return response.data.updateDiscussionComment.comment