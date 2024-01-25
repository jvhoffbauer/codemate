def get_graphql_translation_discussion_comments(
    *, settings: Settings, discussion_number: int
):
    comment_nodes: List[Comment] = []
    discussion_edges = get_graphql_translation_discussion_comments_edges(
        settings=settings, discussion_number=discussion_number
    )

    while discussion_edges:
        for discussion_edge in discussion_edges:
            comment_nodes.append(discussion_edge.node)
        last_edge = discussion_edges[-1]
        discussion_edges = get_graphql_translation_discussion_comments_edges(
            settings=settings,
            discussion_number=discussion_number,
            after=last_edge.cursor,
        )
    return comment_nodes