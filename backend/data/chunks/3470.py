        @app.post("/", response_model=test_type)
        def post_endpoint(input: test_type):
            return input