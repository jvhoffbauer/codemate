- This method is a private (underscore prefixed) function called `_minzoom`.
- It returns the value of the `minzoom` attribute from the TMS object associated with this MapboxGL instance.
- The returned value represents the minimum zoom level supported by the map's tile server, which can be used to prevent users from zooming too far out and encountering missing or low-resolution tiles.