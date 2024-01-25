    def gdal_env(disable_read: ReaddirType = Query(ReaddirType.false)):
        return {"GDAL_DISABLE_READDIR_ON_OPEN": disable_read.value.upper()}