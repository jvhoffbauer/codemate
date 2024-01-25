        def update_refs(value):
            if not isinstance(value, (dict, list)):
                return

            if isinstance(value, list):
                for v in value:
                    update_refs(v)
                return

            if "$ref" not in value:
                for v in value.values():
                    update_refs(v)
                return

            ref = value["$ref"]
            if ref.startswith(REF_PREFIX):
                *_, schema = ref.split(REF_PREFIX)
                new_schema = old2new_schema_name.get(schema, schema)
                if new_schema != schema:
                    ref = f"{REF_PREFIX}{new_schema}"
                    value["$ref"] = ref