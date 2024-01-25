@router.post("/upload/file", summary="上传图片", name="上传图片")
def upload_image(
    file: UploadFile = File(...),
):
    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    # 建议计算并记录一次 文件md5值 避免重复存储相同资源
    save_dir = f"{settings.BASE_PATH}/static/img"

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return resp.ok(data={"image": f"/static/img/{tmp_file_name}"})