- Retrieves locations from confirmed, deaths, and recovered categories using `get_category`.
- Combines and formats the retrieved locations into a list called `locations`, which is returned at the end.
- Assumes that the indices of columns remain consistent across different versions of the dataset. If this assumption breaks due to changes in the dataset structure, it could lead to critical errors.