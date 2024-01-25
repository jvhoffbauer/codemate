    def __call__(self, img: ImageData) -> ImageData:
        """Encode DEM into RGB."""
        data = numpy.clip(img.data[0] + 32768.0, 0.0, 65535.0)
        r = data / 256
        g = data % 256
        b = (data * 256) % 256
        arr = numpy.stack([r, g, b]).astype(numpy.uint8)

        return ImageData(
            arr,
            img.mask,
            assets=img.assets,
            crs=img.crs,
            bounds=img.bounds,
        )