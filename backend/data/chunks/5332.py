async def date_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="release-date",
        name="Release date",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DATE,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )
    for value in [
        datetime.datetime(2020, 10, 5),
        datetime.datetime(2020, 11, 5),
    ]:
        adal.add(
            AttributeValue,
            attribute=attribute,
            name=f"{attribute.name}: {value.date()}",
            slug=f"{value.date()}_{attribute.id}",
            value=f"{value.date()}",
        )
    await adal.commit()

    return attribute