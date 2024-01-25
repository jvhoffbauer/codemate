    def __call__(self, img: ImageData) -> ImageData:
        """Apply Multiplication factor."""
        # Multiply image data bcy factor
        data = img.data * self.factor

        # Create output ImageData
        return ImageData(
            data,
            img.mask,
            assets=img.assets,
            crs=img.crs,
            bounds=img.bounds,
        )