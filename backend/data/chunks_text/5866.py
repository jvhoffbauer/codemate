- Defines a function `valid_database_url_` that takes in class `cls` and dictionary `values`.
- Sets the default value for `amis_image_receiver` and `amis_file_receiver` using the site path provided by `values`.
- Checks whether `database_url` or `database_url_async` is already present in `values`, and sets it to `sqlite+aiosqlite:///amisadmin.db?check_same_thread=False` as the default URL if neither of them are found.