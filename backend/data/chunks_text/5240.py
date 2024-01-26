- Defines a dataclass called `AssetsBidxParams`, which is derived from `AssetsParams`.
- Contains two optional query parameters: `asset_indexes` and `asset_expression`.
- The `asset_indexes` parameter allows specifying per-asset band indexes as a comma-separated list or range (e.g., `"data|1;2;3"`). These values are stored in a dictionary with the asset name as key.
- The `asset_expression` parameter allows specifying per-asset band expressions using the same syntax as Pandas label slicing (e.g., `"data|b1*b2+b3"`). These expressions are also stored in a dictionary with the asset name as key.