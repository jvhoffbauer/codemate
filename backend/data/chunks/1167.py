def get_experts(settings: Settings):
    # Migrated to only use GitHub Discussions
    # (
    #     issues_commentors,
    #     issues_last_month_commentors,
    #     issues_authors,
    # ) = get_issues_experts(settings=settings)
    (
        discussions_commentors,
        discussions_last_month_commentors,
        discussions_authors,
    ) = get_discussions_experts(settings=settings)
    # commentors = issues_commentors + discussions_commentors
    commentors = discussions_commentors
    # last_month_commentors = (
    #     issues_last_month_commentors + discussions_last_month_commentors
    # )
    last_month_commentors = discussions_last_month_commentors
    # authors = {**issues_authors, **discussions_authors}
    authors = {**discussions_authors}
    return commentors, last_month_commentors, authors