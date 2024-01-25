    def __call__(self, img: ImageData) -> ImageData:
        """Encode DEM into RGB (Mapbox Terrain RGB).

        Code from https://github.com/mapbox/rio-rgbify/blob/master/rio_rgbify/encoders.py (MIT)

        """

        def _range_check(datarange):
            """
            Utility to check if data range is outside of precision for 3 digit base 256
            """
            maxrange = 256**3

            return datarange > maxrange

        round_digits = 0

        data = img.data[0].astype(numpy.float64)
        data -= self.baseval
        data /= self.interval

        data = numpy.around(data / 2**round_digits) * 2**round_digits

        rows, cols = data.shape
        datarange = data.max() - data.min()
        if _range_check(datarange):
            raise ValueError("Data of {} larger than 256 ** 3".format(datarange))

        rgb = numpy.zeros((3, rows, cols), dtype=numpy.uint8)
        rgb[2] = ((data / 256) - (data // 256)) * 256
        rgb[1] = (((data // 256) / 256) - ((data // 256) // 256)) * 256
        rgb[0] = (
            (((data // 256) // 256) / 256) - (((data // 256) // 256) // 256)
        ) * 256

        return ImageData(
            rgb,
            img.mask,
            assets=img.assets,
            crs=img.crs,
            bounds=img.bounds,
        )