        @factory.router.get("/validate", response_model=Info)
        def validate(
            src_path: str = Depends(factory.path_dependency),
            strict: bool = Query(False, description="Treat warnings as errors"),
        ):
            """Validate a COG"""
            return cog_info(src_path, strict=strict)