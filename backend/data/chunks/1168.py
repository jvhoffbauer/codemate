def get_contributors(settings: Settings):
    pr_nodes: List[PullRequestNode] = []
    pr_edges = get_graphql_pr_edges(settings=settings)

    while pr_edges:
        for edge in pr_edges:
            pr_nodes.append(edge.node)
        last_edge = pr_edges[-1]
        pr_edges = get_graphql_pr_edges(settings=settings, after=last_edge.cursor)

    contributors = Counter()
    commentors = Counter()
    reviewers = Counter()
    authors: Dict[str, Author] = {}

    for pr in pr_nodes:
        author_name = None
        if pr.author:
            authors[pr.author.login] = pr.author
            author_name = pr.author.login
        pr_commentors: Set[str] = set()
        pr_reviewers: Set[str] = set()
        for comment in pr.comments.nodes:
            if comment.author:
                authors[comment.author.login] = comment.author
                if comment.author.login == author_name:
                    continue
                pr_commentors.add(comment.author.login)
        for author_name in pr_commentors:
            commentors[author_name] += 1
        for review in pr.reviews.nodes:
            if review.author:
                authors[review.author.login] = review.author
                pr_reviewers.add(review.author.login)
        for reviewer in pr_reviewers:
            reviewers[reviewer] += 1
        if pr.state == "MERGED" and pr.author:
            contributors[pr.author.login] += 1
    return contributors, commentors, reviewers, authors