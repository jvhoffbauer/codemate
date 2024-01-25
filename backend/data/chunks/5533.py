    def __call__(self, img: ImageData) -> ImageData:
        """Normalized difference."""
        b1 = img.data[0].astype("float32")
        b2 = img.data[1].astype("float32")

        arr = numpy.where(img.mask, (b2 - b1) / (b2 + b1), 0)

        # ImageData only accept image in form of (count, height, width)
        arr = numpy.expand_dims(arr, axis=0).astype(self.output_dtype)

        return ImageData(
            arr,
            img.mask,
            assets=img.assets,
            crs=img.crs,
            bounds=img.bounds,
        )