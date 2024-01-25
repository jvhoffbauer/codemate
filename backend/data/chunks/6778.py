    def get_openrpc(self):
        methods_spec = []
        schemas_spec = {}
        errors_by_code = defaultdict(set)
        ref_template = "#/components/schemas/{model}"

        for route in self.routes:
            if not isinstance(route, MethodRoute):
                continue

            params_schema = route.params_model.model_json_schema(
                ref_template=ref_template
            )

            if isinstance(route.result_model, BaseModel):
                result_schema = route.result_model.model_json_schema(
                    ref_template=ref_template
                )
            else:
                result_model = create_model(
                    f"{route.name}_Result", result=(route.result_model or Any, ...)
                )
                result_schema = result_model.model_json_schema(
                    ref_template=ref_template
                )

            for error in route.errors:
                errors_by_code[error.CODE].add(error)

            method_spec = {
                "name": route.name,
                "params": [
                    {
                        "name": param_name,
                        "schema": param_schema,
                        "required": param_name in params_schema.get("required", []),
                    }
                    for param_name, param_schema in params_schema["properties"].items()
                ],
                "result": {
                    "name": result_schema["title"],
                    "schema": result_schema["properties"]["result"],
                },
                "tags": [
                    {
                        "name": tag,
                    }
                    for tag in route.tags
                ],
                "errors": [
                    {
                        "$ref": f"#/components/errors/{code}",
                    }
                    for code in sorted({error.CODE for error in route.errors})
                ],
            }
            if route.summary:
                method_spec["summary"] = route.summary

            methods_spec.append(method_spec)
            schemas_spec.update(params_schema.get("$defs", {}))
            schemas_spec.update(result_schema.get("$defs", {}))

        errors_spec = {}
        for code, errors in errors_by_code.items():
            assert errors
            first, *_ = errors
            spec = {
                "code": code,
                "message": first.MESSAGE,
            }

            error_models = []
            for error in errors:
                error_model = error.get_data_model()
                if error_model is not None:
                    error_models.append(error_model)

            if error_models:
                if len(error_models) == 1:
                    error_schema = error_models[0].schema(ref_template=ref_template)
                else:
                    # Data schemes of multiple error objects with same code
                    # are merged together in a single schema
                    error_models.sort(key=lambda m: m.__name__)
                    error_schema = pydantic.TypeAdapter(
                        Union[tuple(error_models)]
                    ).json_schema(
                        ref_template=ref_template,
                    )
                    error_schema["title"] = f"ERROR_{code}"

                schemas_spec.update(error_schema.pop("$defs", {}))
                spec["data"] = error_schema

            errors_spec[str(code)] = spec

        return {
            "openrpc": "1.2.6",
            "info": {
                "version": self.version,
                "title": self.title,
            },
            "servers": self.servers,
            "methods": methods_spec,
            "components": {
                "schemas": schemas_spec,
                "errors": errors_spec,
            },
        }