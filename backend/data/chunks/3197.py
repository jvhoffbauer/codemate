        @app.post("/example/")
        def example(item: Item = Body(example={"data": "Data in Body example"})):
            return item