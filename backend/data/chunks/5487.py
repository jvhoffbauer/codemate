        @self.router.get(
            "/algorithms",
            response_model=Dict[str, AlgorithmMetadata],
            summary="Retrieve the list of available Algorithms.",
            operation_id="getAlgorithms",
        )
        def available_algorithms(request: Request):
            """Retrieve the list of available Algorithms."""
            return {k: metadata(v) for k, v in self.supported_algorithm.data.items()}