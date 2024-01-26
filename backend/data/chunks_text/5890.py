- This function is called `get_deny_fields`, which returns a set of denied (unauthorized) fields based on the given request and action.
- It first checks whether there's already a cached result for this specific action from the current request using the key `f"{self.unique_id}_exclude_fields"`. If so, it directly returns that set.
- Otherwise, it initializes an empty dictionary `check_fields` to store the list/filter/create/update/read permission fields depending on the action type.
- Then it iterates over all these permission fields and filters out those without authorization by calling another asynchronous method `has_field_permission`. The resulting unauthorized fields are added into a new set `fields`.
- Finally, it caches both the original request scope and the newly computed `fields` under the same key `f"{self.unique_id}_exclude_fields"` for future requests with similar actions.