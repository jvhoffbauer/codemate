- Takes a byte array `content` representing an image file
- Uses Python's built-in `MemoryFile` class to read the contents of the byte array into memory without writing it to disk
- Returns a dictionary containing two keys:
   - The metadata profile extracted from the image using GDAL (Geospatial Data Abstraction Library), which is stored in the destination dataset created by opening the input stream with `mem.open()`
   - A list representation of the bounds or extent of the image, also obtained through GDAL

2. How can I use this function to extract metadata and bounds from a GeoTIFF image that has been loaded into a variable called `image_data`? Provide an example usage statement.