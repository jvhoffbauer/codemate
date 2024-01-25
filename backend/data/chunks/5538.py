    @property
    def dependency(self):
        """FastAPI PostProcess dependency."""

        def post_process(
            algorithm: Literal[tuple(self.data.keys())] = Query(
                None, description="Algorithm name"
            ),
            algorithm_params: str = Query(None, description="Algorithm parameter"),
        ) -> Optional[BaseAlgorithm]:
            """Data Post-Processing options."""
            kwargs = json.loads(algorithm_params) if algorithm_params else {}
            if algorithm:
                try:
                    return self.get(algorithm)(**kwargs)

                except ValidationError as e:
                    raise HTTPException(status_code=400, detail=str(e)) from e

            return None

        return post_process