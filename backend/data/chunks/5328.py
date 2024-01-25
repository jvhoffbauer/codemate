async def color_attribute(session: AsyncSession):
    adal = AsyncDal(session)
    attribute = adal.add(
        Attribute,
        slug="color",
        name="Color",
        type=Attribute.Type.PRODUCT,
        input_type=Attribute.InputType.DROPDOWN,
        filterable_in_storefront=True,
        filterable_in_dashboard=True,
        available_in_grid=True,
    )
    adal.add(AttributeValue, attribute=attribute, name="Red", slug="red", value="red")
    adal.add(
        AttributeValue, attribute=attribute, name="Blue", slug="blue", value="blue"
    )
    await adal.commit()
    return attribute