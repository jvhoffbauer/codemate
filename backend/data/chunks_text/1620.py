- This endpoint is accessed using the GET method and has a path of "/users/"
- It returns an instance of `CommonsDep`, which contains commonly used data across multiple endpoints in the application
- The `CommonsDep` class can be defined as follows:
   - @dataclasses.dataclass()
   - class CommonsDep:
       - db: Session = Depends(db.session)
       - current_user: User = Depends(auth.get_current_user())
       - logger: Logger = Depends(get_logger)
```