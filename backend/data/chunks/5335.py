@pytest.fixture(scope="session")
async def product_type(session: AsyncSession, color_attribute, size_attribute):
    adal = AsyncDal(session)
    product_type = adal.add(
        ProductType,
        name="Default Type",
        slug="default-type",
        has_variants=True,
        is_shipping_required=True,
        weight=0.1,
        is_digital=True,
    )
    adal.add(
        AttributeProduct,
        attribute=color_attribute,
        product_type=product_type,
    )
    adal.add(
        AttributeProduct,
        attribute=size_attribute,
        product_type=product_type,
    )
    await adal.commit()
    return product_type