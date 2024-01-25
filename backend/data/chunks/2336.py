def sub_duplicate_dependency(
    item: Item, sub_item: Item = Depends(duplicate_dependency)
):
    return [item, sub_item]