    @app.get("/get_custom_class")
    def return_some_user():
        # Test that the fix also works for custom pydantic classes
        return SomeCustomClass(a_uuid=MyUuid("b8799909-f914-42de-91bc-95c819218d01"))