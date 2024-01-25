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