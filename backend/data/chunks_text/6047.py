- Creates an `AdminGroup` object and retrieves it from the `AdminSite`.
- Adds two child objects (`DocsAdmin` and `TmpLinkAdmin`) to the `AdminGroup`.
- Tests appending and removing child objects using methods of both the `AdminGroup` and the `AdminSite`.
- Verifies that getting a list of all child objects works correctly for both the `AdminGroup` and the `AdminSite`, with recursive traversal handled by the latter.