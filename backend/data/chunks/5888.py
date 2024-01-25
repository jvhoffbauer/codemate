    def AnnotatedItemIdList(self):
        """Annotated Item ID List, used to filter the id of the data that the user has permission to operate on.
        And automatically perform fastapi dependency injection
        """
        return Annotated[List[str], Depends(self.filtered_item_id)]