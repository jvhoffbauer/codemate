async def no_duplicates_sub(
    item: Item, sub_items: List[Item] = Depends(sub_duplicate_dependency)
):
    return [item, sub_items]