- Tests the `/stac/info` and `/stac/info.geojson` endpoints for retrieving item metadata with optional asset selection using mocks for HTTP requests and rasterio functions. - Verifies that assets can be selected individually or as a list, and that they are included in the resulting JSON object. - Checks that the correct content type is returned when requesting a GeoJSON representation of the item's geometry and associated assets.