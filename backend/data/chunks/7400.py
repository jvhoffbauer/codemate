def paginator(query: ModelSelect, page: int, page_size: int, order_by: str = "id ASC"):
    count = query.count()
    if page < 1:
        page = 1

    if page_size <= 0:
        page_size = 10

    if page_size >= 100:
        page_size = 100

    if page == 1:
        offset = 0
    else:
        offset = (page - 1) * page_size

    query = query.offset(offset).limit(page_size).order_by(SQL(order_by))

    total_pages = math.ceil(count / page_size)

    paginate = {
        "total_pages": total_pages,
        "count": count,
        "current_page": page,
        "pre_page": page - 1 if page > 1 else page,
        "next_page": page if page == total_pages else page + 1,
    }

    return list(query.dicts()), paginate