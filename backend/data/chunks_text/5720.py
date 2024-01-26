- Defines a cached property called `router_path` for the current object (presumably a subclass of Starlette's `BaseSettings`)
- If the current object's `router` attribute matches the app's default router, returns the path to that router
- Otherwise, concatenates the path to the app's default router with the prefix of the current object's `router` attribute