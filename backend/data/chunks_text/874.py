- Defines a function `deep_dict_update()` that takes two dictionaries as arguments - `main_dict` and `update_dict`.
- Iterates through all keys of `update_dict`, updating corresponding values in `main_dict` based on certain conditions.
- If the key exists in both dictionaries and is a nested dictionary, recursively calls itself to perform an update at that level.
- If the key exists in both dictionaries but has different data types (i.e., one is a list), appends the new list to the existing list.
- Otherwise, simply replaces the old value with the new one.