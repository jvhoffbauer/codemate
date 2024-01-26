- Decorates a method with middleware using Flask-EP's `@ep.method` decorator
- Specifies a single middleware function to be applied before executing the decorated method (stored in variable `middleware`)
- Returns a string value when the decorated method is called