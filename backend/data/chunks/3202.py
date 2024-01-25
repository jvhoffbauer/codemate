        def example_examples(
            item: Item = Body(
                example={"data": "Overridden example"},
                examples=[
                    {"data": "examples example_examples 1"},
                    {"data": "examples example_examples 2"},
                ],
            ),
        ):
            return item