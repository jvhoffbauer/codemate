- Registers one or more `BaseAdminT` classes as admins using the `register_model()` method of the current site's registry (stored in `self`)
- Updates a dictionary called `_registered` with keys being each registered class and values being `None`
- Returns the first registered class passed to the function