async def size_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="size",
        name="Size",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DROPDOWN,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )
    adal.add(AttributeValue, attribute=attribute, name="3XL", slug="3xl", value="3xl")
    adal.add(AttributeValue, attribute=attribute, name="2XL", slug="2xl", value="2xl")
    adal.add(AttributeValue, attribute=attribute, name="XL", slug="xl", value="xl")
    adal.add(AttributeValue, attribute=attribute, name="L", slug="l", value="l")
    await adal.commit()
    return attribute