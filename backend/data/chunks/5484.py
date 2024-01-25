@dataclass
class AlgorithmFactory:
    """Algorithm endpoints Factory."""

    # Supported algorithm
    supported_algorithm: Algorithms = available_algorithms

    # FastAPI router
    router: APIRouter = field(default_factory=APIRouter)

    def __post_init__(self):
        """Post Init: register routes"""

        def metadata(algorithm: BaseAlgorithm) -> AlgorithmMetadata:
            """Algorithm Metadata"""
            props = algorithm.schema()["properties"]

            # Inputs Metadata
            ins = {
                k.replace("input_", ""): v["default"]
                for k, v in props.items()
                if k.startswith("input_") and "default" in v
            }

            # Output Metadata
            outs = {
                k.replace("output_", ""): v["default"]
                for k, v in props.items()
                if k.startswith("output_") and "default" in v
            }

            # Algorithm Parameters
            params = {
                k: v
                for k, v in props.items()
                if not k.startswith("input_") and not k.startswith("output_")
            }
            return AlgorithmMetadata(inputs=ins, outputs=outs, parameters=params)

        @self.router.get(
            "/algorithms",
            response_model=Dict[str, AlgorithmMetadata],
            summary="Retrieve the list of available Algorithms.",
            operation_id="getAlgorithms",
        )
        def available_algorithms(request: Request):
            """Retrieve the list of available Algorithms."""
            return {k: metadata(v) for k, v in self.supported_algorithm.data.items()}

        @self.router.get(
            "/algorithms/{algorithmId}",
            response_model=AlgorithmMetadata,
            summary="Retrieve the metadata of the specified algorithm.",
            operation_id="getAlgorithm",
        )
        def algorithm_metadata(
            algorithm: Literal[tuple(self.supported_algorithm.list())] = Path(
                ..., description="Algorithm name", alias="algorithmId"
            ),
        ):
            """Retrieve the metadata of the specified algorithm."""
            return metadata(self.supported_algorithm.get(algorithm))