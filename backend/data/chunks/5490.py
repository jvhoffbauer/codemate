        def algorithm_metadata(
            algorithm: Literal[tuple(self.supported_algorithm.list())] = Path(
                ..., description="Algorithm name", alias="algorithmId"
            ),
        ):
            """Retrieve the metadata of the specified algorithm."""
            return metadata(self.supported_algorithm.get(algorithm))