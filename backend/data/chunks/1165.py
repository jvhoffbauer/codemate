def get_issues_experts(settings: Settings):
    issue_nodes: List[IssuesNode] = []
    issue_edges = get_graphql_issue_edges(settings=settings)

    while issue_edges:
        for edge in issue_edges:
            issue_nodes.append(edge.node)
        last_edge = issue_edges[-1]
        issue_edges = get_graphql_issue_edges(settings=settings, after=last_edge.cursor)

    commentors = Counter()
    last_month_commentors = Counter()
    authors: Dict[str, Author] = {}

    now = datetime.now(tz=timezone.utc)
    one_month_ago = now - timedelta(days=30)

    for issue in issue_nodes:
        issue_author_name = None
        if issue.author:
            authors[issue.author.login] = issue.author
            issue_author_name = issue.author.login
        issue_commentors = set()
        for comment in issue.comments.nodes:
            if comment.author:
                authors[comment.author.login] = comment.author
                if comment.author.login != issue_author_name:
                    issue_commentors.add(comment.author.login)
        for author_name in issue_commentors:
            commentors[author_name] += 1
            if issue.createdAt > one_month_ago:
                last_month_commentors[author_name] += 1

    return commentors, last_month_commentors, authors