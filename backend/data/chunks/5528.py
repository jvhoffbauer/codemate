    def __call__(self, img: ImageData) -> ImageData:
        """Create hillshade from DEM dataset."""
        data = img.data[0]
        mask = img.mask
        bounds = img.bounds

        x, y = numpy.gradient(data)

        slope = numpy.pi / 2.0 - numpy.arctan(numpy.sqrt(x * x + y * y))
        aspect = numpy.arctan2(-x, y)
        azimuthrad = self.azimuth * numpy.pi / 180.0
        altituderad = self.angle_altitude * numpy.pi / 180.0
        shaded = numpy.sin(altituderad) * numpy.sin(slope) + numpy.cos(
            altituderad
        ) * numpy.cos(slope) * numpy.cos(azimuthrad - aspect)
        hillshade_array = 255 * (shaded + 1) / 2

        data = numpy.expand_dims(hillshade_array, axis=0).astype(dtype=numpy.uint8)

        if self.buffer:
            data = data[:, self.buffer : -self.buffer, self.buffer : -self.buffer]
            mask = mask[self.buffer : -self.buffer, self.buffer : -self.buffer]
            # image bounds without buffer
            window = windows.Window(
                col_off=self.buffer,
                row_off=self.buffer,
                width=mask.shape[1],
                height=mask.shape[0],
            )
            bounds = windows.bounds(window, img.transform)

        return ImageData(
            data,
            mask,
            assets=img.assets,
            crs=img.crs,
            bounds=bounds,
        )