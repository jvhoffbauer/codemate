def get_top_users(
    *,
    counter: Counter,
    min_count: int,
    authors: Dict[str, Author],
    skip_users: Container[str],
):
    users = []
    for commentor, count in counter.most_common(50):
        if commentor in skip_users:
            continue
        if count >= min_count:
            author = authors[commentor]
            users.append(
                {
                    "login": commentor,
                    "count": count,
                    "avatarUrl": author.avatarUrl,
                    "url": author.url,
                }
            )
    return users