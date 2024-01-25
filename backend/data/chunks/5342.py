async def test_filtering_by_attribute(
    session: AsyncSession,
    product_type,
    # color_attribute,
    # size_attribute,
    # # category,
    # date_attribute,
    # date_time_attribute,
    # # boolean_attribute,
):
    adal = AsyncDal(session)
    assert len(await adal.all(ProductType)) == 1
    ...