def get_discussions_experts(settings: Settings):
    discussion_nodes: List[DiscussionsNode] = []
    discussion_edges = get_graphql_question_discussion_edges(settings=settings)

    while discussion_edges:
        for discussion_edge in discussion_edges:
            discussion_nodes.append(discussion_edge.node)
        last_edge = discussion_edges[-1]
        discussion_edges = get_graphql_question_discussion_edges(
            settings=settings, after=last_edge.cursor
        )

    commentors = Counter()
    last_month_commentors = Counter()
    authors: Dict[str, Author] = {}

    now = datetime.now(tz=timezone.utc)
    one_month_ago = now - timedelta(days=30)

    for discussion in discussion_nodes:
        discussion_author_name = None
        if discussion.author:
            authors[discussion.author.login] = discussion.author
            discussion_author_name = discussion.author.login
        discussion_commentors = set()
        for comment in discussion.comments.nodes:
            if comment.author:
                authors[comment.author.login] = comment.author
                if comment.author.login != discussion_author_name:
                    discussion_commentors.add(comment.author.login)
            for reply in comment.replies.nodes:
                if reply.author:
                    authors[reply.author.login] = reply.author
                    if reply.author.login != discussion_author_name:
                        discussion_commentors.add(reply.author.login)
        for author_name in discussion_commentors:
            commentors[author_name] += 1
            if discussion.createdAt > one_month_ago:
                last_month_commentors[author_name] += 1
    return commentors, last_month_commentors, authors