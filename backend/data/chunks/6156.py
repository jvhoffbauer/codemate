    def delete_item(self, obj: SchemaModelT) -> None:
        obj.delete_time = datetime.now()