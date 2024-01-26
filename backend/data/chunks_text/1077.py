1. Retrieves a list of DiscussionsNodes and their edges using GraphQL API (get_graphql_question_discussion_edges).
2. Traverses through the graph to retrieve all discussions and their related comments and replies.
3. Counts the number of times each user has commented on any discussion or its replies (stored in `commentors`) and also counts the number of times they have commented within the past month (stored in `last_month_commentors`).
4. Maintains a dictionary of Authors with their corresponding login names (`authors`).