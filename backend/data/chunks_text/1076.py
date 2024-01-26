- Retrieves a list of issues and their edges using GraphQL queries (get_graphql_issue_edges function not shown here).
- Uses a counter to keep track of the number of comments made by each user (commentors dictionary).
- Also keeps track of the number of comments made by users within the past month (last_month_commentors dictionary).
- Maintains a dictionary of all authors encountered during this process (authors dictionary).
- Extracts the login name of the author associated with an issue (if any), as well as those associated with its comments (using a set to avoid duplicates).
- Updates both dictionaries accordingly based on whether or not the issue was created more than a month ago.